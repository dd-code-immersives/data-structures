import random
from copy import copy

class Tree:

	def __init__(self, data):
		self.left = None
		self.right =  None
		self.data = data 


	def get_min_val(self):

		min_val = -1
		curr = None
		curr = self.left 
		while curr:
			min_val = curr.data
			curr = curr.left
		return min_val


	def get_min_val_t(self):

		return self.in_order_traversal()[0]

	def get_max_val(self):

		max_val = -1
		curr = None
		curr = self.right
		while curr:
			max_val = curr.data
			curr = curr.right
		return max_val

	def get_max_val_t(self):

		return self.in_order_traversal()[-1]


	def in_order_traversal(self, elems=None):


		if elems is None:
			elems = []

		# left 
		if self.left:
			self.left.in_order_traversal(elems)

		# root
		elems.append(self.data)

		# right
		if self.right:
			self.right.in_order_traversal(elems)

		return elems
		


	def pre_order_traversal(self, elems=None):

		if elems is None:
			elems = []

		# root
		elems.append(self.data)

		# left 
		if self.left:
			self.left.pre_order_traversal(elems)

		# right 
		if self.right:
			self.right.pre_order_traversal(elems)
		
		return elems

	def post_order_traversal(self, elems=None):

		if elems is None:
			elems = []

		# left 
		if self.left:
			self.left.post_order_traversal(elems)

		# right 
		if self.right:
			self.right.post_order_traversal(elems)

		# root 
		elems.append(self.data)

		return elems

	def traverse(self, algo="pre"):

		if algo == "pre":
			res = self.pre_order_traversal()
		elif algo == "post":
			res =  self.post_order_traversal()
		else:
			res = self.in_order_traversal()
		return res

	def insert(self, data):

		# self.data  = 3, data = 6
		if self.data:

			# i.e. 6 < 3
			if data < self.data:

				if not self.left:
					self.left = Tree(data)
				else:
					# self.left.insert(6)
					# self.left = 3
					self.left.insert(data)

			# i.e. 10 > 8
			elif data > self.data:

				if not self.right:
					self.right = Tree(data)
				else:
					self.right.insert(data)

		else:
			self.data = data


	def search(self, val, path=str()):

		# BASE CASE
		if val == self.data:
			path += str(self.data)
			return True, path
		
		# GENERAL CASE  

		# if val is less than the current node, recurse left 
		if val < self.data and self.left:

			path += str(self.data)
			path += "-"
			return self.left.search(val, path)

		# if val is greater than the current node, recurse right
		elif val > self.data and self.right:

			path += str(self.data)
			path += "-"
			return self.right.search(val, path)

		return False, str()

	def get_level(self, val, level=0):

		if val == self.data:
			return level

		if val < self.data and self.left:
			level += 1
			return self.left.get_level(val, level)

		# if val is greater than the current node, recurse right
		elif val > self.data and self.right:
			level += 1
			return self.right.get_level(val, level)

		return -1

	def is_identical(self, tree2):
		return self.traverse() == tree2.traverse()

	def is_full_tree(self):

		# BASE CASE 

		# if both are None, we are either at the bottom of the tree
		# or the root has no children 
		if not self.left and not self.right:
			return True 

		# the node has two children , keep checking each recursively
		if self.left and self.right:
			return self.left.is_full_tree() and self.right.is_full_tree()

		# if self.left and not self.right return false
		return False

	def has_child_sum_property(self):

		if not self.left and not self.right:
			return True 

		left, right = 0,0
		if self.right:
			right = self.right.data
		if self.left:
			left = self.left.data

		if right + left == self.data:
			return self.left.has_child_sum_property() and self.right.has_child_sum_property()

		return False



	def __str__(self):

		res = self.traverse()
		return " ".join(map(str, res))





if __name__ == '__main__':

	
	# nodes = [i for i in range(1, 11)]
	# root = Tree(2)
	# root.insert(1)
	# root.insert(3)
	# root.insert(4)
	# root.insert(6)

	# rooti = Tree(2)
	# rooti.insert(1)
	# rooti.insert(3)
	# rooti.insert(4)
	# rooti.insert(6)

	# # is_found, path = root.search(6)
	# # print(path)


	# root2 = Tree(9)
	# root2.insert(5)
	# root2.insert(7)
	# root2.insert(8)

	# root3 = Tree(8)
	# root3.insert(3)
	# root3.insert(10)
	# root3.insert(6)
	# print(root3.traverse())

	# root4 = Tree(8)
	# root4.left = Tree(3)
	# root4.right = Tree(10)
	# root4.left.right = Tree(6)
	# print(root4.traverse())


	# if root3.is_identical(root4):
	# 	print("trees are identical")
	# else:
	# 	print("not identical")

	# root = Tree(10)
	# root.insert(12)
	# root.insert(25)
	# root.insert(30)
	# root.insert(15)
	# root.insert(36)
	# print(root.in_order_traversal())



	# print(root.is_identical(rooti))
	# print(root.is_identical(root2))

	# # print(root.pre_order_traversal())
	# # print(root.post_order_traversal())
	# # print(root.in_order_traversal())
	# print(root.get_min_val_t())
	# print(root.get_min_val())
	# print(root.get_max_val_t())
	# print(root.get_max_val())
	# is_found, path = root2.search(8)
	# print(path)


	#print(is_identical(root, root2))
	# print(root.in_order_traversal()) # -> 1,2,3
	# print("------------------")
	# print(root.pre_order_traversal()) # -> 2,1,3
	# print("-------------------")
	# print(root.post_order_traversal()) # -> 1,3,2
	# print("-------------------")
	# print(root.search(6))
	# print(root.get_level(20))
	#print(root.traverse())
	#print(root)

	tree = Tree(2)
	tree.left = Tree(1)
	tree.right = Tree(3) 

	print(tree.in_order_traversal())
	print(tree.pre_order_traversal())
	print(tree.post_order_traversal())

	print(tree)
	print(f"is full tree: { tree.is_full_tree() }")

	tree = None

	tree = Tree(8)
	tree.left = Tree(3)
	tree.left.left = Tree(1)
	tree.left.right = Tree(6)
	tree.left.right.left = Tree(4)
	tree.left.right.right = Tree(7)
	tree.right = Tree(10)
	tree.right.right = Tree(14)
	tree.right.right.left = Tree(13)

	print(tree)
	print(f"is full tree: { tree.is_full_tree() }")


	# print(tree.in_order_traversal())
	# print(tree.pre_order_traversal())
	# print(tree.post_order_traversal())


