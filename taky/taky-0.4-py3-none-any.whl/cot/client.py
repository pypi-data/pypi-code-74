import logging
from datetime import datetime, timedelta

from lxml import etree

from taky import cot
from taky.util import XMLDeclStrip

class TAKClient(object):
    def __init__(self, sock, router=None):
        self.sock = sock
        self.router = router
        self.user = cot.TAKUser()

        self.xdc = XMLDeclStrip()
        self.parser = etree.XMLPullParser(tag='event', resolve_entities=False)
        self.parser.feed(b'<root>')

        self.lgr = logging.getLogger(TAKClient.__name__)

    def __repr__(self):
        # IPv6 returns a 4 element tuple
        (ip, port) = self.sock.getpeername()[:2]
        return f'<TAKClient uid={self.user.uid} callsign={self.user.callsign} client={ip}:{port}>'

    def feed(self, data):
        data = self.xdc.feed(data)
        try:
            self.parser.feed(self.xdc.feed(data))
        except etree.XMLSyntaxError as e:
            self.lgr.warn("XML Parsing Error: %s", e)

        for (etype, elm) in self.parser.read_events():
            #self.lgr.debug(etree.tostring(elm))
            try:
                evt = cot.Event.from_elm(elm)
            except (ValueError, TypeError) as e:
                self.lgr.warn("Unable to parse element: %s", e)
                continue

            self.lgr.debug(evt)
            if evt.etype.startswith('a'):
                self.handle_atom(evt)
            elif evt.etype.startswith('b'):
                self.handle_bits(evt)
            elif evt.etype.startswith('t'):
                self.handle_tasking(evt)
            else:
                # Don't know what to do with these yet!
                self.handle_marti(evt)
            elm.clear(keep_tail=True)

    def handle_atom(self, evt):
        if evt.detail is None:
            return

        if evt.detail.find('takv') is not None:
            first_ident = self.user.update_from_evt(evt)
            self.router.push_event(self, self.user.as_element)

            if first_ident:
                self.router.client_ident(self)

            return

        self.handle_marti(evt)

    def handle_bits(self, evt):
        if evt.etype == 'b-t-f':
            # Currently, ATAK 4.2.0.4 does not properly set MARTI for chat
            # messages sent to teams. In any case, setting the destination as a
            # cot.Teams prevents queue-ing multiple messages in the routing
            # engine

            chat = cot.GeoChat.from_elm(evt)
            if chat.src is None:
                chat.src = self.router.find_client(uid=chat.src_uid)
            if chat.dst is None:
                chat.dst = self.router.find_client(uid=chat.dst_uid)

            if self.user is not chat.src:
                self.lgr.warn("%s is sending messages for user %s", self.user, chat.src)
            if isinstance(chat.dst, cot.Teams) and self.user.group != chat.dst:
                self.lgr.warn("%s is sending messages for group %s", self.user, chat.src)

            if chat.src is not None and chat.dst is not None:
                self.router.push_event(src=chat.src, event=chat.event, dst=chat.dst)
                return

        self.handle_marti(evt)

    def handle_tasking(self, elm):
        if elm.etype == 't-x-c-t':
            self.pong()
            return

        self.handle_marti(evt)

    def handle_marti(self, evt):
        if evt.detail is None:
            return

        marti = evt.detail.find('marti')
        if marti is not None:
            for dest in marti.iterfind('dest'):
                callsign = dest.get('callsign')
                dst = self.router.find_client(callsign=callsign)
                if dst is None:
                    continue
                self.router.push_event(self, evt, dst)
        else:
            self.router.push_event(self, evt)


    def pong(self):
        now = datetime.utcnow()
        pong = cot.Event(
            uid='takPong',
            etype='t-x-c-t-r',
            how='h-g-i-g-o',
            time=now,
            start=now,
            stale=now + timedelta(seconds=20)
        )
        self.router.push_event(self, pong, dst=self)
