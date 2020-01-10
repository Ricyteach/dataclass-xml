# dataclass-xml
A simple library for combining dataclasses and xml functionality

```pydocstring
>>> from dataclass_xml import DataclassElement
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
>>> n.tag # xml api
'node'
>>> n.x # dcls api
'0'
```