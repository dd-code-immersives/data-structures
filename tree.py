import random
from copy import copy

class Tree:

	def __init__(self, data):
		self.left = None
		self.right =  None
		self.data = data 


	def in_order_traversal(self, elems = []):

		# left 
		if self.left:
			self.left.in_order_traversal()

		# root
		elems.append(self.data)

		# right
		if self.right:
			self.right.in_order_traversal()

		return elems
		


	def pre_order_traversal(self, elems = []):

		# root
		print(f"state of elems {elems}")
		elems.append(self.data)

		# left 
		if self.left:
			self.left.pre_order_traversal()

		# right 
		if self.right:
			self.right.pre_order_traversal()

		return elems

	def post_order_traversal(self, elems = []):

		# left 
		if self.left:
			self.left.post_order_traversal()

		# right 
		if self.right:
			self.right.post_order_traversal()

		# root 
		elems.append(self.data)

		res = copy(elems)

		del elems
		return res

	def traverse(self, algo="inorder"):

		if algo == "pre":
			return self.pre_order_traversal()
		elif algo == "post":
			return self.post_order_traversal()
		else:
			return self.in_order_traversal()

	def insert(self, data):

		if self.data:

			# i.e. 3 < 8
			if data < self.data:

				if not self.left:
					self.left = Tree(data)
				else:
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


	# def __str__(self):

	# 	res = self.traverse()
	# 	return " ".join(map(str, res))





def is_identical(tree1, tree2):
	# res1 = self.traverse()
	# res2 = tree.traverse() 
	# print(res1)
	# print(res2)
	# if res1 == res2:
	# 	return True
	# return False
	print(tree1.traverse())
	print()
	print(tree2.traverse())
	return len(tree1.traverse()) == len(tree2.traverse())



if __name__ == '__main__':

	
	# nodes = [i for i in range(1, 11)]
	root = Tree(2)
	root.insert(1)
	root.insert(3)
	root.insert(4)
	root.insert(6)


	# is_found, path = root.search(6)
	# print(path)

	print(root.pre_order_traversal())

	root2 = Tree(9)
	root2.insert(5)
	root2.insert(7)
	root2.insert(8)
	print(dir())
	print(root2.pre_order_traversal())



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