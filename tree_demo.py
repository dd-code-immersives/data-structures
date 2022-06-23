


class Tree:
	""" 
	A Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties

	One node is marked as Root node
	Every node other than the root is associated with one parent node.
	Each node can have any amount of children nodes

	"""

	def __init__(self, data, left=None, right=None):
		self.data = data
		self.left = None 
		self.right  = None


	def insert(self, data):

		if data == self.data:
			raise ValueError("Can't insert duplicate values")

		# if the value is smaller it goes to the left 

		if data < self.data:
			if not self.left:
				self.left = Tree(data)
			else:
				self.left.insert(data)

		# if the value is greater it goes to the right  
		elif data > self.data:
			if not self.right:
				self.right = Tree(data)
			else:
				self.right.insert(data)

	# def __str__(self):
	# 	return f"Tree: {self.root}"
	def print_tree(self):

		if self.left:
			self.left.print_tree()

		print(self.data)

		if self.right:
			self.right.print_tree()


if __name__ == '__main__':
	tree = Tree(8)
	tree.insert(3)
	tree.insert(10)
	tree.insert(14)
	tree.insert(6)
	print(tree.data)
	print(tree.left.data)
	print(tree.right.data)
	print(tree.right.right.data)
	print(tree.left.right.data)




