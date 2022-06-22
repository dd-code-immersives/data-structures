
class Node():

	def __init__(self, data, next_= None, prev_= None):
		self.data = data
		self.next = next_
		self.prev = prev_

	def __str__(self):
		return f"Node({self.data})"

class LinkedList():

	SEPARATOR = "->"

	def __init__(self, MAX=5):
		self.head = None
		self.size = 0
		self.max = MAX


	def contains(self, elem):

		# if the list is empty, the element definitely is not in the list
		if self.is_empty():
			return False
		else:
			curr = self.head
			while curr:
				if curr.data == elem:
					return True
				curr = curr.next

		return False

	def insert(self, node):

		""" 
		 case 1: linkedlist is empty -> set head to node 
		 case 2: linkedlist is not empty, 
		 		 1. look at the next node , while it's not none, 
		 		 2. keep "iterating" or going to the next node 
		 		 	curr = curr.next 
		 		 3. if curr.next == None, break out of the loop
		 		 4. set curr.next equal to the new node
		 		 5. we have inserted into the end of the linked list
		"""

		if self.is_empty():
			self.head = node
		elif self.size == self.max:
			raise Exception(f"Max capacity {self.size} exceeded, Insert failed!")
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = node

		self.size += 1

	def delete(self, data):
		""" 
		1. locate the node we want to delete
		2. point the previous node to the next node 
		3. this derefences the node we want to delete 

		case 1: deleting the first one, make the next node the head node.
		case 2: see steps 1-3
		"""

		if self.is_empty():
			return
		else:

			curr = self.head

			# if it's at the front of the list, set the node to the next element
			if curr.data == data:
				self.head = curr.next
				return

			while curr:
				# the next node is the one we want to get rid of
				if curr.next.data == data:
					old_val = curr.next
					curr.next = curr.next.next
					print(f"Deleted {old_val}")
					self.size -= 1
					break
				curr = curr.next


	def is_empty(self):
		if not self.head:
			return True
		return False

	def length(self):
		""" 
		case 1: if the linked list is empty return 0
		case 2: iterate over the list till the end, incrementing the counter as we go 
		
		"""
		# counter  = 0

		# if self.is_empty(self):
		#    return 0 
		# else:
		# 	curr = self.head
		# 	while curr:
		# 		counter += 1
		# 		curr = curr.next

		# return counter
		return self.size

	def __str__(self):
		res = str()

		if self.is_empty():
			return "List is empty"
		else:
			curr = self.head
			while curr:
				res += curr.data

				# if there is a following element , append a separator
				if curr.next:
					res += self.SEPARATOR

				curr = curr.next

		return res



class DoublyLinkedList(LinkedList):

	SEPARATOR = "<->"


	def __check_safe_index(self, index):
		if index < 0 or index > self.length():
			raise IndexError("invalid Index")


	def insert_at_beginning(self, data):

		# the case where it is empty, and we just set the HEAD of the linkedlist
		if self.is_empty():
			node = Node(data, self.head, None)
			self.head = node

		# the case where it is not empty, we make the new node the head, and point the 
		# previous head to the new one.
		else:
			node = Node(data, self.head, None) 
			self.head.prev = node
		self.size += 1

	def insert_at_end(self, data):

		if self.is_empty():
		   self.head = Node(data, None, None)
		   self.size += 1
		   return

		itr = self.head
		# iterate until we hit the end of the list 
		while itr.next:
			itr = itr.next

		itr.next = Node(data, None, itr)

		self.size += 1
		

	def insert_at(self, index, data):
		
		# make sure the index is valid, if not, throw error
		self.__check_safe_index(index)

		if index == 0:
			self.insert_at_beginning(data)

		count = 0
		itr = self.head 
		while itr:
			if count == index - 1:

				# push the node forward for the index where we want to insert
				node = Node(data, next_=itr.next, prev_=itr)
				if node.next:
					# make the next node (which we pushed forward) point to our new node
					node.next.prev = node
				itr.next = node
				break

			itr = itr.next
			count += 1


	def remove_at(self, index):

		self.__check_safe_index(index)

		if index == 0:
			self.head = self.head.next
			self.head.prev = None

		curr_index = 0
		itr = self.head 
		while itr:
			if curr_index == index:
				#skips over node we want to delete at index
				itr.prev.next = itr.next 
				if itr.next:

					# if the next element from the one we are deleting 
					# is not None, we set it's previous pointer to the element before
					# our current 
					# B <-> C <-> D
					# B <-> D
					itr.next.prev = itr.prev
				break

			# iterate to the next element
			# keep track of count
			itr = itr.next 
			curr_index += 1

	def remove(self, val):

		if not self.contains(val):
			raise ValueError("Value not Found")

		itr = self.head 

		# if it's in the beginning
		if self.head.data == val:
			self.head = self.head.next
			self.head.prev = None 
			return 

		while itr:
			if itr.data == val:
				

				itr.prev.next = itr.next 
				if itr.next:

					# if the next element from the one we are deleting 
					# is not None, we set it's previous pointer to the element before
					# our current 
					# B <-> C <-> D
					# B <-> D
					itr.next.prev = itr.prev
				break

			# iterate to the next element
			# keep track of count
			itr = itr.next 


	def insert_values(self, data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)
		

	def get_last_node(self):
		itr = self.head

		# while the next node is not None, we haven't reached the end of the list
		while itr.next:
			itr = itr.next

		# once we reach the end, return the last value 
		return itr




if __name__ == '__main__':
	node_a = Node("A")
	node_b = Node("B")
	node_c = Node("C")
	nodes = [ch for ch in "ABCDE"]

	# node_a.next = node_b
	# node_b.next = node_c

	# # print(node_a.data)
	# # print(node_a.next.data)
	# # print(node_a.next.next.data)
	# # print(node_a)
	# # print(node_b)
	# # print(node_c)

	# linked_list = LinkedList()
	# #print(linked_list.is_empty())
	# #print(linked_list.contains(node_a))

	# # populate linked list
	# for node in nodes:
	# 	linked_list.insert(node) 

	# print(linked_list)
	# linked_list.delete("D")
	# print(linked_list)

	dll = DoublyLinkedList()
	dll.insert_values(nodes)

	print(dll)
	#print(dll.length())
	dll.insert_at(2, "NEW")
	print("inserting new element at index 2")
	print(dll)
	print("removing element at index 2")
	dll.remove_at(2)
	print(dll)
	print(dll.contains("C"))
	print(dll.contains("J"))
	dll.remove("C")
	dll.remove("A")
	print(dll)

	

