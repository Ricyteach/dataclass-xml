import pytest
from dataclasses import dataclass
from dataclass_xml import DataclassElement


@pytest.fixture
def parent_el_fixture():
    @dataclass
    class ParentElement(DataclassElement):
        pass
    return ParentElement


@pytest.fixture
def node_cls_fixture(parent_el_fixture):
    @dataclass
    class Node(parent_el_fixture, tag="node"):
        x: str
        y: str
    return Node


def test_abstract_parent(parent_el_fixture):
    with pytest.raises(TypeError):
        parent_el_fixture()


def test_node_basic(node_cls_fixture):
    n = node_cls_fixture("0", "0")
    assert n.tag == 'node' # xml api
    assert n.get('x') == '0' # xml api
    assert n.x == "0" # dcls api
