# dataclass-xml
A simple library for combining dataclasses and xml functionality

Allows creation of XML-based classes containing data fluently:

```python
from dataclasses import dataclass
from dataclass_xml import DataclassElement


@dataclass
class ParentElement(DataclassElement):
    pass


@dataclass
class Node(ParentElement, tag="node"):
    """XML element representing a node.
    <node x="0" y="0" />
    """
    x: str
    y: str
```

Now both the dataclasses and element tree APIs are available io the resulting objects:

```pydocstring
>>> n = Node("0", "0")
>>> n
Node(x='0', y='0')
>>> n.tag # xml api
'node'
>>> n.x # dcls api
'0'
```
