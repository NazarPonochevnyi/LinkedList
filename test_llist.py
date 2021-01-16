import pytest
from linked_list import Node, LinkedList

def test_node_init_str_repr():
    first_node = Node(1)
    second_node = Node('a')
    assert str(first_node) == '1'
    assert repr(second_node) == 'Node(a)'

def test_llist_init_str_repr():
    first_node = Node(1)
    second_node = Node('a')
    llist = LinkedList()
    assert str(llist) == 'None'
    assert repr(llist) == 'LinkedList()'
    llist.head = first_node
    first_node.next = second_node
    assert str(llist) == '1 -> a -> None'
    assert repr(llist) == 'LinkedList(1, a)'
    llist = LinkedList([2, 'b'])
    assert str(llist) == '2 -> b -> None'
    assert repr(llist) == 'LinkedList(2, b)'

def test_iter():
    llist = LinkedList()
    assert [item for item in llist] == []
    llist = LinkedList([3, 'c', -10.9])
    assert list(map(str, llist)) == ['3', 'c', '-10.9']

def test_appendleft():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    llist.appendleft(0)
    assert repr(llist) == 'LinkedList(0)'
    llist.appendleft('car')
    assert repr(llist) == 'LinkedList(car, 0)'
    llist.appendleft(-2.1)
    assert repr(llist) == 'LinkedList(-2.1, car, 0)'

def test_append():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    llist.append(0)
    assert repr(llist) == 'LinkedList(0)'
    llist.append('car')
    assert repr(llist) == 'LinkedList(0, car)'
    llist.append(-2.1)
    assert repr(llist) == 'LinkedList(0, car, -2.1)'

def test_insert():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    llist.insert(0, 'car')
    assert repr(llist) == 'LinkedList(car)'
    llist.insert(100, 0)
    assert repr(llist) == 'LinkedList(car, 0)'
    llist.insert(-100, 10)
    assert repr(llist) == 'LinkedList(10, car, 0)'
    llist.insert(1, 2)
    assert repr(llist) == 'LinkedList(10, 2, car, 0)'
    llist.insert(3, -4.4)
    assert repr(llist) == 'LinkedList(10, 2, car, -4.4, 0)'

def test_remove():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    with pytest.raises(Exception):
        llist.remove(99.5)
    llist = LinkedList([10, 2, 'car', -4.4, 0])
    assert repr(llist) == 'LinkedList(10, 2, car, -4.4, 0)'
    llist.remove(10)
    assert repr(llist) == 'LinkedList(2, car, -4.4, 0)'
    llist.remove(0)
    assert repr(llist) == 'LinkedList(2, car, -4.4)'
    llist.remove('car')
    assert repr(llist) == 'LinkedList(2, -4.4)'
    with pytest.raises(Exception):
        llist.remove(-1)

def test_getitem():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    with pytest.raises(Exception):
        llist[0]
    llist = LinkedList([-10.1, 2, 'car', 4.4, 0])
    assert llist[0] == -10.1
    assert llist[4] == 0
    assert llist[2] == 'car'
    with pytest.raises(IndexError):
        llist[100]
    with pytest.raises(IndexError):
        llist[-1]

def test_setitem():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    with pytest.raises(Exception):
        llist[0] = 0
    llist = LinkedList([10, 2, 'car', 4.4, 0])
    assert repr(llist) == 'LinkedList(10, 2, car, 4.4, 0)'
    llist[0] = -10.1
    assert repr(llist) == 'LinkedList(-10.1, 2, car, 4.4, 0)'
    llist[4] = 1
    assert repr(llist) == 'LinkedList(-10.1, 2, car, 4.4, 1)'
    llist[2] = 'cat'
    assert repr(llist) == 'LinkedList(-10.1, 2, cat, 4.4, 1)'
    with pytest.raises(IndexError):
        llist[100] = 100
    with pytest.raises(IndexError):
        llist[-1] = -1

def test_delitem():
    llist = LinkedList()
    assert repr(llist) == 'LinkedList()'
    with pytest.raises(Exception):
        del llist[0]
    llist = LinkedList([-10.1, 2, 'car', 4.4, 0])
    assert repr(llist) == 'LinkedList(-10.1, 2, car, 4.4, 0)'
    del llist[0]
    assert repr(llist) == 'LinkedList(2, car, 4.4, 0)'
    del llist[3]
    assert repr(llist) == 'LinkedList(2, car, 4.4)'
    del llist[1]
    assert repr(llist) == 'LinkedList(2, 4.4)'
    with pytest.raises(IndexError):
        del llist[100]
    with pytest.raises(IndexError):
        del llist[-1]
