'''
This program is the Implemention of Dynamic Singly Linked List Data Structure. 
 
data : The value of the Node
next: pointer which points to next element of a node
head: pointer which points to first element of the node
tail: pointer which points to last element of the Node

ADT:

insertElementAtBeginning: insert given element in the beginning of list.
insertElementAtaPosition: insert given element at a given position.
insertElementAtEnd: insert given element at the end.            
printChoice: user interaction for operations
peekList: showing the Linked List elements.
Example: 
|A| --> |B| -->|C|
head Pointer: points to A
tail Pointer : points to C
 
'''
class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SinglyLinkedList(Node):
	
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def insertElementAtBeginning(self):
			
		element = int(input("Enter the element: "))
		new_node = Node(element)
		new_node.next = self.head
		self.head = new_node
		self.size += 1
		if self.size == 1:
			self.tail = new_node
		
	def insertElementAtaPosition(self):
		
		print("insertElementAtaPosition")
		print("Note: The list current size is: ",self.size) 
		position = int(input("Enter the position: "))
		
		if position == 0:
			self.insertElementAtBeginning()

		elif position == self.size:
			self.insertElementAtEnd()
		elif position > self.size:
			print("position out of bound")
		else: 
			element = int(input("Enter the element: "))	
			temp = self.head
			current_position = 0
			while (current_position == position):
				current_position +=1
				temp = temp.next
			print("new element is inserted after: ", temp.data)
			new_node = Node(element)
			new_node.next = temp.next
			temp.next = new_node
			self.size += 1

	
	def insertElementAtEnd(self):
		print("insertElementAtEnd")
		element = int (input("Enter the element: "))
		new_node = Node(element)
		self.tail.next = new_node
		self.tail= new_node
		self.size += 1
		

	def print_choice(self):
		print("Singly Linked List Implementation")
		print("Choose a option from the below list:")
		arg = 0
		while (arg != 4):
			arg = int(input("1: Insert an element\n2: Delete an element\n3: Peek the list\nPress 4 to exit\n"))
		
			if arg == 1:
				choice = int(input("press 1 if you want insert element at the beginning: \npress 2 if you want insert element at a position: \npress 3 if you want to insert element at the end:\n"))
				if choice == 1: 
					operation = getattr(self,'insertElementAtBeginning',lambda :'Invalid')
					operation()

				elif choice == 2:
					operation = getattr(self,'insertElementAtaPosition',lambda :'Invalid')
					operation()
				
				elif choice == 3:
					operation = getattr(self,'insertElementAtEnd',lambda :'Invalid')
					operation()
				else :
					print("Wrong choice try again")

			if arg == 2:
				operation = getattr(self,'deleteData',lambda :'Invalid')
				operation()
	
			if arg == 3:
				operation = getattr(self,'peekList',lambda :'Invalid')
				operation()
	
	def deleteData(self):
		print("deleteData")

	def peekList(self):
			print("The peekList")
			if (self.size == 0):
				print("List Empty\n")
			else:
				print("Head pointer: ",self.head.data)
				print("Tail pointer: ",self.tail.data)
				print("List size: ",self.size) 

				temp = self.head
			
				while(temp!= None):
					print(temp.data,end = '')
					temp = temp.next
					print("-->",end = '')
				print(temp)
				print("End of list")
	
	
if __name__ == '__main__':
	Sllist = SinglyLinkedList()
	Sllist.print_choice()
	
		
