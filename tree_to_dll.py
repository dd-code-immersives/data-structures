from tree import Tree
from linked_list_demo import DoublyLinkedList



def tree_to_dll(tree):

	dll = DoublyLinkedList()
	dll.insert_values(tree.traverse())
	return dll


if __name__ == '__main__':
	tree = Tree(8)
	tree.left = Tree(3)
	tree.left.left = Tree(1)
	tree.left.right = Tree(6)
	tree.left.right.left = Tree(4)
	tree.left.right.right = Tree(7)
	tree.right = Tree(10)
	tree.right.right = Tree(14)
	tree.right.right.left = Tree(13)

	print(tree_to_dll(tree))


	