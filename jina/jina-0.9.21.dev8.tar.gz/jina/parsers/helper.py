import argparse
import os
import uuid

_SHOW_ALL_ARGS = 'JINA_FULL_CLI' in os.environ


def add_arg_group(parser, title):
    return parser.add_argument_group(f'{title} arguments')


def UUIDString(astring):
    """argparse type to check if a string is a valid UUID string"""
    uuid.UUID(astring)
    return astring


class KVAppendAction(argparse.Action):
    """
    argparse action to split an argument into KEY=VALUE form
    on the first = and append to a dictionary.
    This is used for setting up --env
    """

    def __call__(self, parser, args, values, option_string=None):
        import json
        d = getattr(args, self.dest) or {}
        for value in values:
            try:
                d.update(json.loads(value))
            except json.JSONDecodeError:
                try:
                    (k, v) = value.split('=', 2)
                except ValueError:
                    raise argparse.ArgumentTypeError(f'could not parse argument \"{values[0]}\" as k=v format')
                d[k] = v
        setattr(args, self.dest, d)


class DockerKwargsAppendAction(argparse.Action):
    """
    argparse action to split an argument into KEY: VALUE form
    on the first : and append to a dictionary.
    This is used for setting up arbitrary kwargs for docker sdk
    """

    def __call__(self, parser, args, values, option_string=None):
        import json
        d = getattr(args, self.dest) or {}

        for value in values:
            try:
                d.update(json.loads(value))
            except json.JSONDecodeError:
                try:
                    (k, v) = value.split(':', 1)
                except ValueError:
                    raise argparse.ArgumentTypeError(f'could not parse argument \"{values[0]}\" as k:v format')
                # transform from text to actual type (int, list, etc...)
                d[k] = json.loads(v)
        setattr(args, self.dest, d)


class _ColoredHelpFormatter(argparse.ArgumentDefaultsHelpFormatter):
    class _Section(object):

        def __init__(self, formatter, parent, heading=None):
            self.formatter = formatter
            self.parent = parent
            self.heading = heading
            self.items = []

        def format_help(self):
            # format the indented section
            if self.parent is not None:
                self.formatter._indent()
            join = self.formatter._join_parts
            item_help = join([func(*args) for func, args in self.items])
            if self.parent is not None:
                self.formatter._dedent()

            # return nothing if the section was empty
            if not item_help.strip():
                return ''

            # add the heading if the section was non-empty
            if self.heading is not argparse.SUPPRESS and self.heading is not None:
                from ..helper import colored
                current_indent = self.formatter._current_indent
                captial_heading = ' '.join(v[0].upper() + v[1:] for v in self.heading.split(' '))
                heading = '⚙️  %*s%s\n' % (
                    current_indent, '', colored(captial_heading, 'cyan', attrs=['underline', 'bold', 'reverse']))
            else:
                heading = ''

            # join the section-initial newline, the heading and the help
            return join(['\n', heading, item_help, '\n'])

    def start_section(self, heading):
        self._indent()
        section = self._Section(self, self._current_section, heading)
        self._add_item(section.format_help, [])
        self._current_section = section

    def _get_help_string(self, action):
        help_string = ''
        if '%(default)' not in action.help:
            if action.default is not argparse.SUPPRESS:
                from ..helper import colored
                defaulting_nargs = [argparse.OPTIONAL, argparse.ZERO_OR_MORE]
                if isinstance(action, argparse._StoreTrueAction):

                    help_string = colored('default: %s' % (
                        'enabled' if action.default else f'disabled, use "--{action.dest}" to enable it'),
                                          attrs=['dark'])
                elif action.choices:
                    choices_str = f'{{{", ".join([str(c) for c in action.choices])}}}'
                    help_string = colored('choose from: ' + choices_str + '; default: %(default)s', attrs=['dark'])
                elif action.option_strings or action.nargs in defaulting_nargs:
                    help_string = colored('type: %(type)s; default: %(default)s', attrs=['dark'])
        return f'''
        
        {help_string}
        
        {action.help}
        
        '''

    def _join_parts(self, part_strings):
        return '\n' + ''.join([part
                               for part in part_strings
                               if part and part is not argparse.SUPPRESS])

    def _get_default_metavar_for_optional(self, action):
        return ''

    # def _get_default_metavar_for_positional(self, action):
    #     return ''

    def _expand_help(self, action):
        params = dict(vars(action), prog=self._prog)
        for name in list(params):
            if params[name] is argparse.SUPPRESS:
                del params[name]
        for name in list(params):
            if hasattr(params[name], '__name__'):
                params[name] = params[name].__name__
        return self._get_help_string(action) % params

    def _metavar_formatter(self, action, default_metavar):
        if action.metavar is not None:
            result = action.metavar
        elif action.choices is not None:

            if len(action.choices) > 4:
                choice_strs = ', '.join([str(c) for c in action.choices][:4])
                result = f'{{{choice_strs} ... {len(action.choices) - 4} more choices}}'
            else:
                choice_strs = ', '.join([str(c) for c in action.choices])
                result = f'{{{choice_strs}}}'
        else:
            result = default_metavar

        def formatter(tuple_size):
            if isinstance(result, tuple):
                return result
            else:
                return (result,) * tuple_size

        return formatter

    def _split_lines(self, text, width):
        return self._para_reformat(text, width)

    def _fill_text(self, text, width, indent):
        lines = self._para_reformat(text, width)
        return '\n'.join(lines)

    def _indents(self, line):
        """Return line indent level and "sub_indent" for bullet list text."""
        import re
        indent = len(re.match(r'( *)', line).group(1))
        list_match = re.match(r'( *)(([*\-+>]+|\w+\)|\w+\.) +)', line)
        if list_match:
            sub_indent = indent + len(list_match.group(2))
        else:
            sub_indent = indent

        return (indent, sub_indent)

    def _split_paragraphs(self, text):
        """Split text in to paragraphs of like-indented lines."""

        import textwrap, re

        text = textwrap.dedent(text).strip()
        text = re.sub('\n\n[\n]+', '\n\n', text)

        last_sub_indent = None
        paragraphs = list()
        for line in text.splitlines():
            (indent, sub_indent) = self._indents(line)
            is_text = len(line.strip()) > 0

            if is_text and indent == sub_indent == last_sub_indent:
                paragraphs[-1] += ' ' + line
            else:
                paragraphs.append(line)

            if is_text:
                last_sub_indent = sub_indent
            else:
                last_sub_indent = None

        return paragraphs

    def _para_reformat(self, text, width):
        """Reformat text, by paragraph."""

        import textwrap

        lines = list()
        for paragraph in self._split_paragraphs(text):
            (indent, sub_indent) = self._indents(paragraph)

            paragraph = self._whitespace_matcher.sub(' ', paragraph).strip()
            new_lines = textwrap.wrap(
                text=paragraph,
                width=width,
                initial_indent=' ' * indent,
                subsequent_indent=' ' * sub_indent,
            )

            # Blank lines get eaten by textwrap, put it back
            lines.extend(new_lines or [''])

        return lines


_chf = _ColoredHelpFormatter
