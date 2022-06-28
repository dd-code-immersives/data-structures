import pytest 
from linked_list_demo import LinkedList, Node, DoublyLinkedList
from tree import Tree

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

@pytest.fixture
def simple_tree_obj():
	""" 
	2 
   |  | 
   1  3
	"""
	tree = Tree(2)
	tree.left = Tree(1)
	tree.right = Tree(3)

	return tree

@pytest.fixture
def tree_obj():

	tree = Tree(8)
	tree.left = Tree(3)
	tree.left.left = Tree(1)
	tree.left.right = Tree(6)
	tree.left.right.left = Tree(4)
	tree.left.right.right = Tree(7)
	tree.right = Tree(10)
	tree.right.right = Tree(14)
	tree.right.right.left = Tree(13)
	return tree




