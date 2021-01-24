from typing import Iterator, Tuple

import docutils.nodes


def dump_node(node: docutils.nodes.Node) -> str:
    return "\n".join(["    " * indent + line for indent, line in _dump_lines(node)])


def _dump_lines(node: docutils.nodes.Node) -> Iterator[Tuple[int, str]]:
    node_type = type(node).__name__
    head = f"- \x1b[34m{node_type}\x1b[m"
    if isinstance(node, docutils.nodes.Text):
        body = repr(node.astext()[:100])
    else:
        body = str({k: v for k, v in node.attributes.items() if v})
    yield 0, f"{head} {body}"
    for c in node.children:
        for n, l in _dump_lines(c):
            yield n + 1, l
