import json
import logging
import re
from parsel import Selector
import requests
from requests.cookies import merge_cookies, cookiejar_from_dict
from data_factory import Printer, DataGroup, replacer, Replacer

logger = logging.getLogger(__name__)


class Spider(object):
    """
    Process requests params
    """

    # todo add cookie jar dict
    def __init__(self, url, body=None, header=None, cookie=None, overwrite=True, want=None, post_type=None):
        self._url = url
        self._path_dict = {}
        self._param_dict = {}
        self._body_dict = {}
        self._header_dict = {}
        self._cookie_dict = {}
        self.overwrite = overwrite
        self._cookie_jar = requests.cookies.RequestsCookieJar()

        self._resp = None
        self._resp_data = None
        self.others = None
        self.request_kwargs = {}
        self.want = want

        self.method = 'POST' if body else 'GET'
        if self.method == 'POST' and not post_type:
            self.post_type = 'form'
        else:
            self.post_type = post_type

        self._path_str = self._url.split('?')[0]
        self._param_str = '' if body or '?' not in self._url else self._url.split('?')[-1]
        self.str_to_dict(self._url, tag='path')
        self.str_to_dict(self._url, tag='param')

        if isinstance(body, str):
            self._body_str = body or ''
            self.str_to_dict(self._body_str, tag='body')
        else:
            self._body_dict = body if body else {}
            self._body_str = self.body

        if isinstance(header, str):
            self._header_str = header or 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
            self.str_to_dict(self._header_str, tag='header')
        else:
            self._header_dict = header if header else {}

        if isinstance(cookie, str):
            self._cookie_str = cookie or ''
            self.str_to_dict(self._cookie_str, tag='cookie')
        else:
            self._cookie_jar = cookiejar_from_dict(cookie) if cookie else self._cookie_jar

    def clear(self, key=None):
        if key == 'path':
            self._path_dict.clear()
        elif key == 'param':
            self._param_dict.clear()
        elif key == 'header':
            self._header_dict.clear()
        elif key == 'cookie':
            self._cookie_dict.clear()
        elif key == 'cookie_jar' and self._cookie_jar:
            self._cookie_jar.clear()
        elif key is None:
            self._path_dict.clear()
            self._param_dict.clear()
            self._header_dict.clear()
            self._cookie_dict.clear()
            self._cookie_jar.clear()

    # --------------------------------------------------------------------------------- property
    @property
    def status(self):
        if not self.want:
            status_code = self._resp.status_code
            return status_code if status_code == 200 else f'{status_code} {STATUS_INTRODUTION.get(status_code)}'
        else:
            if isinstance(self.want, str):
                result = re.search(self.want, self._resp.text)
                return result.group() if result else None

    @property
    def url(self):
        path = self.path[:-1] if self.path.endswith('/') else self.path
        return path + self.param if self.method == 'GET' else self._url

    @property
    def path(self):
        protocol = self._path_dict.get('protocol')
        domain = self._path_dict.get('domain')
        sub_path = '/'.join([value for key, value in self._path_dict.items() if key not in ['protocol', 'domain']])
        return f'{protocol}://{domain}/{sub_path}'

    @property
    def param(self):
        split_char = '?' if self._param_dict else ''
        param_str = '&'.join([f'{key}={value}' for key, value in self._param_dict.items()]) if self._param_dict else ''
        return split_char + param_str

    @property
    def body(self):
        if self.post_type == 'form':
            return '&'.join([f'{key}={value}' for key, value in self._body_dict.items()])
        elif self.post_type == 'payload':
            return json.dumps(self._body_dict)
        else:
            return ''

    @property
    def headers(self):
        return self._header_dict if self._header_dict else {}

    @property
    def cookies(self):
        self._cookie_dict = self._cookie_jar.get_dict()
        return self._cookie_dict

    @property
    def cookie_jar(self):
        return self._cookie_jar

    @property
    def key_dict(self):
        return {
            'path': list(self._path_dict.keys()),
            'param': list(self._param_dict.keys()),
            'body': list(self._body_dict.keys()),
            'header': list(self._header_dict.keys()),
            'cookie': list(self._cookie_dict.keys()),
        }

    @property
    def resp_data(self):
        if not self._resp_data: self.request()
        return self._resp_data

    # --------------------------------------------------------------------------------- setter
    @url.setter
    def url(self, url):
        self._path_dict = self.str_to_dict(url, tag='path')
        self._param_dict = self.str_to_dict(url, tag='param')

        if self.headers.get('Host'): self.update('Host', self._path_dict.get('domain'), tag='header')

    @path.setter
    def path(self, path):
        if isinstance(path, dict):
            self._path_dict = path
        elif isinstance(path, str):
            self._path_dict = self.str_to_dict(path, tag='path')
        else:
            raise Exception('Type error ... type of path is not dict or str')

    @param.setter
    def param(self, params):
        if isinstance(params, dict):
            self._param_dict = params
        elif isinstance(params, str):
            self._param_dict = self.str_to_dict(params, tag='param')
        else:
            raise Exception('Type error ... type of params is not dict')

    @body.setter
    def body(self, body):
        if isinstance(body, dict):
            self._body_dict = body
        else:
            raise Exception('Type error ... type of body is not dict')

    @headers.setter
    def headers(self, header):
        if isinstance(header, dict):
            self._header_dict = header
        else:
            raise Exception('Type error ... type of header is not dict')

    @cookies.setter
    def cookies(self, cookie):
        if isinstance(cookie, dict):
            self._cookie_jar = cookiejar_from_dict(cookie_dict=cookie, cookiejar=self._cookie_jar,
                                                   overwrite=self.overwrite)
        else:
            raise Exception('Type error ... type of cookie is not dict')

    # --------------------------------------------------------------------------------- core functions
    def request(self, **kwargs):
        self.request_kwargs = kwargs

        if not kwargs.get('method'):
            method = self.method
        else:
            method = kwargs.pop('method')

        if method == 'GET':
            self._resp = requests.get(url=self.url, headers=self.headers, cookies=self.cookies, **kwargs)
        elif method == 'POST':
            self._resp = requests.post(url=self.url, data=self.body, headers=self.headers, cookies=self.cookies,
                                       **kwargs)
        elif method == 'HEAD':
            if self.body:
                self._resp = requests.head(url=self.url, data=self.body, headers=self.headers, cookies=self.cookies,
                                           **kwargs)
            else:
                self._resp = requests.head(url=self.url, headers=self.headers, cookies=self.cookies, **kwargs)
        else:
            raise Exception(f'Method Error ... unsupported method {method}')

        if self._resp.text:
            if '<html' in self._resp.text and '</html>' in self._resp.text:
                self._resp_data = self._resp.text
            else:
                self._resp_data = self._resp.json()
        else:
            print(self.status)

        return self._resp

    def find(self, *rules, dtype=None):
        result = Replacer(*rules, data=self.resp_data, mode='search', dtype=dtype)
        return result.search_result

    def css(self, *rules, extract=True, first=False):
        selector = Selector(self.resp_data)
        result = {}

        if len(rules) == 1 and isinstance(rules[0], str):
            result = selector.css(rules[0])

        elif len(rules) == 1 and isinstance(rules[0], dict):
            for key, css_rule in rules[0].items():
                result[key] = selector.css(css_rule)
        else:
            print(f'Rule Format Error ... unsupported rule format {rules}')

        if extract and isinstance(result, dict):
            for key, value in result.items():
                result[key] = value.extract() if not first else value.extract_first()
        elif extract:
            result = result.extract() if not first else result.extract_first()

        return result

    def update(self, *args, tag=None, request=True):
        """ update tag use args

        tag: param, body, header, cookie
        args: (dict,) or (str,str) or (list,list) or (dict,dict) or (list,list,dict)
        """
        # auto set tag if tag param is not be provide

        if len(args) == 1 and isinstance(args[0], dict):
            for key, value in args[0].items():
                self._update(key, value, tag=tag)

        elif len(args) == 1 and isinstance(args[0], requests.models.Response):
            self._cookie_jar.update(args[0].cookies)

        elif len(args) == 2 and isinstance(args[0], str):
            key, value = args
            self._update(key, value, tag=tag)

        elif len(args) == 2 and isinstance(args[0], list):
            for key, value in zip(args):
                self._update(key, value, tag=tag)

        elif len(args) == 2 and isinstance(args[0], dict):
            for key, value in args[0].items():
                value = args[1].get(value)
                self._update(key, value, tag=tag)
        elif len(args) == 3 and isinstance(args[0], list) and isinstance(args[2], dict):
            for key, value in zip(args[0], args[1]):
                value = args[2].get(value)
                self._update(key, value, tag=tag)
        else:
            raise Exception(f'Update Error ... unsupported update args {args}')

        if request: self.request(**self.request_kwargs)

    def _update(self, key, value, tag=None):
        if not tag:
            for tag_name, key_list in self.key_dict.items():
                if key in key_list:
                    tag = tag_name
                    break
        if not tag:
            tag = 'param' if self.method == 'GET' else 'body'

        if tag == 'param':
            self._param_dict[key] = value
        elif tag == 'body':
            self._body_dict[key] = value
        elif tag == 'header':
            self._header_dict[key] = value
        elif tag == 'cookie':
            self._cookie_jar.set(key, value)
        elif tag == 'path':
            self._path_dict[key] = value

    def str_to_dict(self, string, tag=None):
        """ translate string to dict

        string: url, body, header or cookie
        tag: param, body, header or cookie
        rtype: dict
        """

        if not string: return {}
        if tag == 'path' and self._path_dict: self._path_dict.clear()
        if tag == 'param' and self._param_dict: self._param_dict.clear()
        if tag == 'header' and self._header_dict: self._header_dict.clear()
        if tag == 'cookie' and self._cookie_dict: self._cookie_dict.clear()

        string = string.strip()

        if tag == 'path' and '://' in string:
            if '?' in string: string = string.split('?')[0]

            protocol = string.split('://', 1)[0]
            domain = string.split('://', 1)[1].split('/')[0]
            path_list = string.split('://', 1)[1].split('/')[1:]

            self._path_dict['protocol'] = protocol
            self._path_dict['domain'] = domain
            self._path_dict = {**self._path_dict, **dict(zip([str(i + 1) for i in range(len(path_list))], path_list))}
            return self._path_dict

        if tag == 'param':
            if self.body: return

            # sting : 'https://...?...'
            if '?' in string:
                if '=' in string:
                    string = string.split('?')[-1]
                    self._param_dict = dict(
                        [_.split('=', 1) for _ in string.split('&') if '=' in _ and not _.endswith('=')])
                    self._param_dict = {**self._param_dict, **dict([(_.strip('='), '') for _ in string.split('&')
                                                                    if _.endswith('=') or '=' not in _])}
                else:
                    self._param_dict = dict([(string, string) for _ in string.split('&')])

            # sting : 'name=...'
            elif '=' in string:
                self._param_dict = dict([_.split('=', 1) for _ in string.split('&')])
            else:
                self._param_dict = {}

            return self._param_dict

        if tag == 'body':
            if '=' in string and '&' in string:
                self._body_dict = dict([_.split('=', 1) for _ in string.split('&')])
            elif '=' in string:
                self._body_dict = dict([string.split('=')])
            elif ':' in string:
                self._body_dict = json.loads(string)
            return self._body_dict

        if tag == 'header' or tag == 'cookie':
            split_params = ['\n', ':'] if tag == 'header' else [';', '=']
            target_dict = {}
            for field in string.split(split_params[0]):
                keys = target_dict.keys()

                key, value = field.split(split_params[1], 1)
                key, value = [key.strip(), value.strip()]

                value_in_dict = target_dict.get(key)
                if key in keys and isinstance(value_in_dict, str):
                    target_dict[key] = [value_in_dict, value]
                elif isinstance(value_in_dict, list):
                    target_dict[key].append(value)
                else:
                    target_dict[key] = value

            if tag == 'header': self._header_dict = target_dict
            if tag == 'cookie': self._cookie_jar = cookiejar_from_dict(target_dict)
            return target_dict

    def preview(self, tag=None):
        d_group = DataGroup(name='Params')
        d_group.add_info('url', self.url)
        d_group.add_info('param', self.param)
        d_group.add_info('body', self.body)

        preview_dict = {'headers': self.headers, 'cookies': self.cookies}
        preview_list = ['headers', 'cookies'] if not tag else [tag]

        for key, value in preview_dict.items():
            if key in preview_list:
                d_group.add_data(key, value)
            else:
                continue

        printer = Printer()
        return printer.parse_data_group(d_group)

    def __repr__(self):
        lines = self.preview()
        return '\n'.join(lines)


STATUS_INTRODUTION = {
    100: '客户端应当继续发送请求。这个临时响应是用来通知客户端它的部分请求已经被服务器接收，且仍未被拒绝。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。服务器必须在请求完成后向客户端发送一个最终响应。',
    101: '服务器已经理解了客户端的请求，并将通过Upgrade 消息头通知客户端采用不同的协议来完成这个请求。在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。\n只有在切换新的协议更有好处的时候才应该采取类似措施。例如，切换到新的HTTP 版本比旧版本更有优势，或者切换到一个实时且同步的协议以传送利用此类特性的资源。',
    102: '由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。',
    200: '请求已成功，请求所希望的响应头或数据体将随此响应返回。',
    201: '请求已经被实现，而且有一个新的资源已经依据请求的需要而建立，且其 URI 已经随Location 头信息返回。假如需要的资源无法及时建立的话，应当返回 "202 Accepted"。',
    202: '服务器已接受请求，但尚未处理。正如它可能被拒绝一样，最终该请求可能会也可能不会被执行。在异步操作的场合下，没有比发送这个状态码更方便的做法了。\n返回202状态码的响应的目的是允许服务器接受其他过程的请求（例如某个每天只执行一次的基于批处理的操作），而不必让客户端一直保持与服务器的连接直到批处理操作全部完成。在接受请求处理并返回202状态码的响应应当在返回的实体中包含一些指示处理当前状态的信息，以及指向处理状态监视器或状态预测的指针，以便用户能够估计操作是否已经完成。',
    203: '服务器已成功处理了请求，但返回的实体头部元信息不是在原始服务器上有效的确定集合，而是来自本地或者第三方的拷贝。当前的信息可能是原始版本的子集或者超集。例如，包含资源的元数据可能导致原始服务器知道元信息的超级。使用此状态码不是必须的，而且只有在响应不使用此状态码便会返回200 OK的情况下才是合适的。',
    204: '服务器成功处理了请求，但不需要返回任何实体内容，并且希望返回更新了的元信息。响应可能通过实体头部的形式，返回新的或更新后的元信息。如果存在这些头部信息，则应当与所请求的变量相呼应。\n如果客户端是浏览器的话，那么用户浏览器应保留发送了该请求的页面，而不产生任何文档视图上的变化，即使按照规范新的或更新后的元信息应当被应用到用户浏览器活动视图中的文档。\n由于204响应被禁止包含任何消息体，因此它始终以消息头后的第一个空行结尾。',
    205: '服务器成功处理了请求，且没有返回任何内容。但是与204响应不同，返回此状态码的响应要求请求者重置文档视图。该响应主要是被用于接受用户输入后，立即重置表单，以便用户能够轻松地开始另一次输入。\n与204响应一样，该响应也被禁止包含任何消息体，且以消息头后的第一个空行结束。',
    206: '服务器已经成功处理了部分 GET 请求。类似于 FlashGet 或者迅雷这类的 HTTP 下载工具都是使用此类响应实现断点续传或者将一个大文档分解为多个下载段同时下载。\n该请求必须包含 Range 头信息来指示客户端希望得到的内容范围，并且可能包含 If-Range 来作为请求条件。\n响应必须包含如下的头部域：Content-Range 用以指示本次响应中返回的内容的范围；如果是 Content-Type 为 multipart/byteranges 的多段下载，则每一 multipart 段中都应包含 Content-Range 域用以指示本段的内容范围。假如响应中包含 Content-Length，那么它的数值必须匹配它返回的内容范围的真实字节数。\nDate\nETag 和/或 Content-Location，假如同样的请求本应该返回200响应。\nExpires, Cache-Control，和/或 Vary，假如其值可能与之前相同变量的其他响应对应的值不同的话。\n假如本响应请求使用了 If-Range 强缓存验证，那么本次响应不应该包含其他实体头；假如本响应的请求使用了 If-Range 弱缓存验证，那么本次响应禁止包含其他实体头；这避免了缓存的实体内容和更新了的实体头信息之间的不一致。否则，本响应就应当包含所有本应该返回200响应中应当返回的所有实体头部域。\n假如 ETag 或 Last-Modified 头部不能精确匹配的话，则客户端缓存应禁止将206响应返回的内容与之前任何缓存过的内容组合在一起。\n任何不支持 Range 以及 Content-Range 头的缓存都禁止缓存206响应返回的内容。',
    207: '由WebDAV(RFC 2518)扩展的状态码，代表之后的消息体将是一个XML消息，并且可能依照之前子请求数量的不同，包含一系列独立的响应代码。',
    300: '被请求的资源有一系列可供选择的回馈信息，每个都有自己特定的地址和浏览器驱动的商议信息。用户或浏览器能够自行选择一个首选的地址进行重定向。\n除非这是一个 HEAD 请求，否则该响应应当包括一个资源特性及地址的列表的实体，以便用户或浏览器从中选择最合适的重定向地址。这个实体的格式由 Content-Type 定义的格式所决定。浏览器可能根据响应的格式以及浏览器自身能力，自动作出最合适的选择。当然，RFC 2616规范并没有规定这样的自动选择该如何进行。\n如果服务器本身已经有了首选的回馈选择，那么在 Location 中应当指明这个回馈的 URI；浏览器可能会将这个 Location 值作为自动重定向的地址。此外，除非额外指定，否则这个响应也是可缓存的。',
    301: '被请求的资源已永久移动到新位置，并且将来任何对此资源的引用都应该使用本响应返回的若干个 URI 之一。如果可能，拥有链接编辑功能的客户端应当自动把请求的地址修改为从服务器反馈回来的地址。除非额外指定，否则这个响应也是可缓存的。\n新的永久性的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。\n如果这不是一个 GET 或者 HEAD 请求，因此浏览器禁止自动进行重定向，除非得到用户的确认，因为请求的条件可能因此发生变化。\n注意：对于某些使用 HTTP/1.0 协议的浏览器，当它们发送的 POST 请求得到了一个301响应的话，接下来的重定向请求将会变成 GET 方式。',
    302: '请求的资源现在临时从不同的 URI 响应请求。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。只有在Cache-Control或Expires中进行了指定的情况下，这个响应才是可缓存的。\n新的临时性的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。\n如果这不是一个 GET 或者 HEAD 请求，那么浏览器禁止自动进行重定向，除非得到用户的确认，因为请求的条件可能因此发生变化。\n注意：虽然RFC 1945和RFC 2068规范不允许客户端在重定向时改变请求的方法，但是很多现存的浏览器将302响应视作为303响应，并且使用 GET 方式访问在 Location 中规定的 URI，而无视原先请求的方法。状态码303和307被添加了进来，用以明确服务器期待客户端进行何种反应。',
    303: '对应当前请求的响应可以在另一个 URI 上被找到，而且客户端应当采用 GET 的方式访问那个资源。这个方法的存在主要是为了允许由脚本激活的POST请求输出重定向到一个新的资源。这个新的 URI 不是原始资源的替代引用。同时，303响应禁止被缓存。当然，第二个请求（重定向）可能被缓存。\n新的 URI 应当在响应的 Location 域中返回。除非这是一个 HEAD 请求，否则响应的实体中应当包含指向新的 URI 的超链接及简短说明。\n注意：许多 HTTP/1.1 版以前的 浏览器不能正确理解303状态。如果需要考虑与这些浏览器之间的互动，302状态码应该可以胜任，因为大多数的浏览器处理302响应时的方式恰恰就是上述规范要求客户端处理303响应时应当做的。',
    304: '如果客户端发送了一个带条件的 GET 请求且该请求已被允许，而文档的内容（自上次访问以来或者根据请求的条件）并没有改变，则服务器应当返回这个状态码。304响应禁止包含消息体，因此始终以消息头后的第一个空行结尾。\n该响应必须包含以下的头信息：\nDate，除非这个服务器没有时钟。假如没有时钟的服务器也遵守这些规则，那么代理服务器以及客户端可以自行将 Date 字段添加到接收到的响应头中去（正如RFC 2068中规定的一样），缓存机制将会正常工作。\nETag 和/或 Content-Location，假如同样的请求本应返回200响应。\nExpires, Cache-Control，和/或Vary，假如其值可能与之前相同变量的其他响应对应的值不同的话。\n假如本响应请求使用了强缓存验证，那么本次响应不应该包含其他实体头；否则（例如，某个带条件的 GET 请求使用了弱缓存验证），本次响应禁止包含其他实体头；这避免了缓存了的实体内容和更新了的实体头信息之间的不一致。\n假如某个304响应指明了当前某个实体没有缓存，那么缓存系统必须忽视这个响应，并且重复发送不包含限制条件的请求。\n假如接收到一个要求更新某个缓存条目的304响应，那么缓存系统必须更新整个条目以反映所有在响应中被更新的字段的值。',
    305: '被请求的资源必须通过指定的代理才能被访问。Location 域中将给出指定的代理所在的 URI 信息，接收者需要重复发送一个单独的请求，通过这个代理才能访问相应资源。只有原始服务器才能建立305响应。\n注意：RFC 2068中没有明确305响应是为了重定向一个单独的请求，而且只能被原始服务器建立。忽视这些限制可能导致严重的安全后果。',
    306: '在最新版的规范中，306状态码已经不再被使用。',
    307: '请求的资源现在临时从不同的URI 响应请求。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。只有在Cache-Control或Expires中进行了指定的情况下，这个响应才是可缓存的。\n新的临时性的URI 应当在响应的 Location 域中返回。除非这是一个HEAD 请求，否则响应的实体中应当包含指向新的URI 的超链接及简短说明。因为部分浏览器不能识别307响应，因此需要添加上述必要信息以便用户能够理解并向新的 URI 发出访问请求。\n如果这不是一个GET 或者 HEAD 请求，那么浏览器禁止自动进行重定向，除非得到用户的确认，因为请求的条件可能因此发生变化。/',
    400: '1、语义有误，当前请求无法被服务器理解。除非进行修改，否则客户端不应该重复提交这个请求。\n2、请求参数有误。',
    401: '当前请求需要用户验证。该响应必须包含一个适用于被请求资源的 WWW-Authenticate 信息头用以询问用户信息。客户端可以重复提交一个包含恰当的 Authorization 头信息的请求。如果当前请求已经包含了 Authorization 证书，那么401响应代表着服务器验证已经拒绝了那些证书。如果401响应包含了与前一个响应相同的身份验证询问，且浏览器已经至少尝试了一次验证，那么浏览器应当向用户展示响应中包含的实体信息，因为这个实体信息中可能包含了相关诊断信息。参见RFC 2617。',
    402: '该状态码是为了将来可能的需求而预留的。',
    403: '服务器已经理解请求，但是拒绝执行它。与401响应不同的是，身份验证并不能提供任何帮助，而且这个请求也不应该被重复提交。如果这不是一个 HEAD 请求，而且服务器希望能够讲清楚为何请求不能被执行，那么就应该在实体内描述拒绝的原因。当然服务器也可以返回一个404响应，假如它不希望让客户端获得任何信息。',
    404: '请求失败，请求所希望得到的资源未被在服务器上发现。没有信息能够告诉用户这个状况到底是暂时的还是永久的。假如服务器知道情况的话，应当使用410状态码来告知旧资源因为某些内部的配置机制问题，已经永久的不可用，而且没有任何可以跳转的地址。404这个状态码被广泛应用于当服务器不想揭示到底为何请求被拒绝或者没有其他适合的响应可用的情况下。',
    405: '请求行中指定的请求方法不能被用于请求相应的资源。该响应必须返回一个Allow 头信息用以表示出当前资源能够接受的请求方法的列表。\n鉴于 PUT，DELETE 方法会对服务器上的资源进行写操作，因而绝大部分的网页服务器都不支持或者在默认配置下不允许上述请求方法，对于此类请求均会返回405错误。',
    406: '请求的资源的内容特性无法满足请求头中的条件，因而无法生成响应实体。\n除非这是一个 HEAD 请求，否则该响应就应当返回一个包含可以让用户或者浏览器从中选择最合适的实体特性以及地址列表的实体。实体的格式由 Content-Type 头中定义的媒体类型决定。浏览器可以根据格式及自身能力自行作出最佳选择。但是，规范中并没有定义任何作出此类自动选择的标准。',
    407: '与401响应类似，只不过客户端必须在代理服务器上进行身份验证。代理服务器必须返回一个 Proxy-Authenticate 用以进行身份询问。客户端可以返回一个 Proxy-Authorization 信息头用以验证。参见RFC 2617。',
    408: '请求超时。客户端没有在服务器预备等待的时间内完成一个请求的发送。客户端可以随时再次提交这一请求而无需进行任何更改。',
    409: '由于和被请求的资源的当前状态之间存在冲突，请求无法完成。这个代码只允许用在这样的情况下才能被使用：用户被认为能够解决冲突，并且会重新提交新的请求。该响应应当包含足够的信息以便用户发现冲突的源头。\n冲突通常发生于对 PUT 请求的处理中。例如，在采用版本检查的环境下，某次 PUT 提交的对特定资源的修改请求所附带的版本信息与之前的某个（第三方）请求向冲突，那么此时服务器就应该返回一个409错误，告知用户请求无法完成。此时，响应实体中很可能会包含两个冲突版本之间的差异比较，以便用户重新提交归并以后的新版本。',
    410: '被请求的资源在服务器上已经不再可用，而且没有任何已知的转发地址。这样的状况应当被认为是永久性的。如果可能，拥有链接编辑功能的客户端应当在获得用户许可后删除所有指向这个地址的引用。如果服务器不知道或者无法确定这个状况是否是永久的，那么就应该使用404状态码。除非额外说明，否则这个响应是可缓存的。\n410响应的目的主要是帮助网站管理员维护网站，通知用户该资源已经不再可用，并且服务器拥有者希望所有指向这个资源的远端连接也被删除。这类事件在限时、增值服务中很普遍。同样，410响应也被用于通知客户端在当前服务器站点上，原本属于某个个人的资源已经不再可用。当然，是否需要把所有永久不可用的资源标记为"410 Gone"，以及是否需要保持此标记多长时间，完全取决于服务器拥有者。',
    411: '服务器拒绝在没有定义 Content-Length 头的情况下接受请求。在添加了表明请求消息体长度的有效 Content-Length 头之后，客户端可以再次提交该请求。',
    412: '服务器在验证在请求的头字段中给出先决条件时，没能满足其中的一个或多个。这个状态码允许客户端在获取资源时在请求的元信息（请求头字段数据）中设置先决条件，以此避免该请求方法被应用到其希望的内容以外的资源上。',
    413: '服务器拒绝处理当前请求，因为该请求提交的实体数据大小超过了服务器愿意或者能够处理的范围。此种情况下，服务器可以关闭连接以免客户端继续发送此请求。\n如果这个状况是临时的，服务器应当返回一个 Retry-After 的响应头，以告知客户端可以在多少时间以后重新尝试。',
    414: '请求的URI 长度超过了服务器能够解释的长度，因此服务器拒绝对该请求提供服务。这比较少见，通常的情况包括：\n本应使用POST方法的表单提交变成了GET方法，导致查询字符串（Query String）过长。\n重定向URI “黑洞”，例如每次重定向把旧的 URI 作为新的 URI 的一部分，导致在若干次重定向后 URI 超长。\n客户端正在尝试利用某些服务器中存在的安全漏洞攻击服务器。这类服务器使用固定长度的缓冲读取或操作请求的 URI，当 GET 后的参数超过某个数值后，可能会产生缓冲区溢出，导致任意代码被执行[1]。没有此类漏洞的服务器，应当返回414状态码。',
    415: '对于当前请求的方法和所请求的资源，请求中提交的实体并不是服务器中所支持的格式，因此请求被拒绝。',
    416: '如果请求中包含了 Range 请求头，并且 Range 中指定的任何数据范围都与当前资源的可用范围不重合，同时请求中又没有定义 If-Range 请求头，那么服务器就应当返回416状态码。\n假如 Range 使用的是字节范围，那么这种情况就是指请求指定的所有数据范围的首字节位置都超过了当前资源的长度。服务器也应当在返回416状态码的同时，包含一个 Content-Range 实体头，用以指明当前资源的长度。这个响应也被禁止使用 multipart/byteranges 作为其 Content-Type。',
    417: '在请求头 Expect 中指定的预期内容无法被服务器满足，或者这个服务器是一个代理服务器，它有明显的证据证明在当前路由的下一个节点上，Expect 的内容无法被满足。',
    421: '从当前客户端所在的IP地址到服务器的连接数超过了服务器许可的最大范围。通常，这里的IP地址指的是从服务器上看到的客户端地址（比如用户的网关或者代理服务器地址）。在这种情况下，连接数的计算可能涉及到不止一个终端用户。',
    422: '从当前客户端所在的IP地址到服务器的连接数超过了服务器许可的最大范围。通常，这里的IP地址指的是从服务器上看到的客户端地址（比如用户的网关或者代理服务器地址）。在这种情况下，连接数的计算可能涉及到不止一个终端用户。或者请求格式正确，但是由于含有语义错误，无法响应。（RFC 4918 WebDAV）423 Locked\n当前资源被锁定。（RFC 4918 WebDAV）',
    424: '由于之前的某个请求发生的错误，导致当前请求失败，例如 PROPPATCH。（RFC 4918 WebDAV）',
    425: '在WebDav Advanced Collections 草案中定义，但是未出现在《WebDAV 顺序集协议》（RFC 3658）中。',
    426: '客户端应当切换到TLS/1.0。（RFC 2817）',
    449: '由微软扩展，代表请求应当在执行完适当的操作后进行重试。',
    500: '服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器的程序码出错时出现。',
    501: '服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。',
    502: '作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。',
    503: '由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。如果能够预计延迟时间，那么响应中可以包含一个 Retry-After 头用以标明这个延迟时间。如果没有给出这个 Retry-After 信息，那么客户端应当以处理500响应的方式处理它。\n注意：503状态码的存在并不意味着服务器在过载的时候必须使用它。某些服务器只不过是希望拒绝客户端的连接。',
    504: '作为网关或者代理工作的服务器尝试执行请求时，未能及时从上游服务器（URI标识出的服务器，例如HTTP、FTP、LDAP）或者辅助服务器（例如DNS）收到响应。\n注意：某些代理服务器在DNS查询超时时会返回400或者500错误',
    505: '服务器不支持，或者拒绝支持在请求中使用的 HTTP 版本。这暗示着服务器不能或不愿使用与客户端相同的版本。响应中应当包含一个描述了为何版本不被支持以及服务器支持哪些协议的实体。',
    506: '由《透明内容协商协议》（RFC 2295）扩展，代表服务器存在内部配置错误：被请求的协商变元资源被配置为在透明内容协商中使用自己，因此在一个协商处理中不是一个合适的重点。',
    507: '服务器无法存储完成请求所必须的内容。这个状况被认为是临时的。WebDAV (RFC 4918)',
    509: '服务器达到带宽限制。这不是一个官方的状态码，但是仍被广泛使用。',
    510: '获取资源所需要的策略并没有没满足。（RFC 2774）',
}
