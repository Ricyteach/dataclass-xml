from dataclasses import dataclass, asdict
import xml.etree.ElementTree as xml
from typing import ClassVar


@dataclass
class DataclassElement(xml.Element):
    """A dataclass-compatible xml.etree.Element class.

    >>> @dataclass
    ... class ParentElement(DataclassElement):
    ...     pass
    ...
    >>> @dataclass
    ... class Node(ParentElement, tag="node"):
    ...     x: str
    ...     y: str
    ...
    >>> n = Node("0", "0")
    >>> n
    Node(x='0', y='0')
    >>> n.tag # xml api works
    'node'
    >>> n.get("x") # xml api works
    '0'
    >>> n.x # dcls api works
    '0'
    """
    element_tag: ClassVar[str]

    def __init_subclass__(cls, tag: str = None, **kwargs) -> None:
        if tag is not None:
            cls.element_tag = tag

    def __post_init__(self) -> None:
        try:
            super().__init__(self.element_tag, **asdict(self))
        except AttributeError as e:
            raise TypeError(f"cannot instantiate {type(self).__qualname__}") from e
