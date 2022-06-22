import pytest 
from linked_list_demo import LinkedList, Node, DoublyLinkedList

@pytest.fixture
def linked_list_obj():
	return LinkedList()

@pytest.fixture
def linked_list_obj_elems():
	nodes = [Node(ch) for ch in "ABCD"]
	linked_list = LinkedList()
	linked_list.head = nodes[0]
	linked_list.head.next = nodes[1]
	linked_list.head.next.next = nodes[2]
	linked_list.head.next.next.next = nodes[3]

	return linked_list


@pytest.fixture
def doubly_linked_list_obj():
	return DoublyLinkedList()

# @pytest.fixture
# def node_obj():
# 	return Node()

