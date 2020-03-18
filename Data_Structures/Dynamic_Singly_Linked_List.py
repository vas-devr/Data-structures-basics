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
		
		print("LOG:Inserting an Element At a Position")
		print("LOG: The list current size is: ",self.size) 
		position = int(input("Enter the position: "))
		
		if position == 0:
			self.insertElementAtBeginning()

		elif position == self.size:
			self.insertElementAtEnd()
		elif position > self.size:
			print("ERR: position out of bound")
		else: 
			element = int(input("Enter the element: "))	
			temp = self.head
			current_position = 0
			while (current_position == position):
				current_position +=1
				temp = temp.next
			print("LOG: New element is inserted after: ", temp.data)
			new_node = Node(element)
			new_node.next = temp.next
			temp.next = new_node
			self.size += 1

	
	def insertElementAtEnd(self):
		print("LOG: Inserting an Element At the End")
		element = int (input("Enter the element: "))
		new_node = Node(element)
		if self.size == 0:
			self.head = new_node
			self.tail = new_node
			self.size +=1
		else:
			self.tail.next = new_node
			self.tail= new_node
			self.size += 1

	def deleteElementfromList(self,element,temp):
		print("LOG: Deleting an element from list")
		#temp = self.head.next
		
		prev = temp
		print("Before prev:", prev.data,"temp:",temp.data )
		while(temp != None):
			if (temp.data == element):
				break

			prev = temp
			temp = temp.next
		print("prev:", prev.data,"temp:",temp.data )
		if temp == None:
			return

		if self.size == 2 and self.head.next == temp.data:
			print("here1")
			self.tail = self.head

		elif temp.data == element:
			print("here2")
			self.tail = prev
		else:
			print("here3")
			self.tail = temp.next

		prev.next = temp.next
		self.size -= 1
		self.tail = temp.next
		print("After removing links : prev:", prev.data,"temp:",temp.data,"self.tail ",self.tail.data )
		temp = None
           
	def deleteElementInBegining(self,element):
		#print("LOG: Deleting element in the beginning")
		temp = self.head
		if temp.data == element:
			#temp = self.head.next
			if temp.next == None:
				self.head = None
				self.size -=1
				#print ("self.size",self.size)
				return 1,temp
			else:
				#print("NEXT", temp.next.next)
				self.head = temp.next
				temp.next = temp.next.next
				self.size -=1
				#print("temp.data" , temp.data)
				#print ("self.size",self.size)
				return 1, temp
				
				'''	
				self.head.next = temp.next
				self.head = temp
				self.size -=1
				return 1,temp
				'''
		else:
			return 0,temp


	def deleteElement(self):
		print("LOG: Delete an Element")
		#print("self.size",self.size)
		if self.size == 0:
			print("ERR: The List is Empty, Cannot delete")
			return
		else:
			self.peekList()
			element = int (input("Enter the element you want to delete: "))
			res,temp = self.deleteElementInBegining(element)
			#print (res,temp.data)
			if res == 0:
				self.deleteElementfromList(element,temp)	


	def print_choice(self):
		print('{:^100s}'.format("Singly Linked List Implementation"))
		print("\nChoose a option from the below list:")
		arg = 0
		while (arg != 4):
			arg = int(input("1: Insert an element\n2: Delete an element\n3: Peek the list\nPress 4 to exit\n"))
		
			if arg == 1:
				choice = int(input("press 1 if you want insert element at the beginning: \npress 2 if you want insert element at a position: \npress 3 if you want to insert element at the end:\nInput: "))
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
					print("LOG: Wrong choice try again")

			if arg == 2:
				operation = getattr(self,'deleteElement',lambda :'Invalid')
				operation()
	
			if arg == 3:
				operation = getattr(self,'peekList',lambda :'Invalid')
				operation()
	
	def peekList(self):
			print('{:^50s}'.format("LOG: The current List"))
			if (self.size == 0):
				print("\nERR: List Empty\n")
			else:
				print("\nLOG: Head pointer: ",self.head.data)
				print("LOG: Tail pointer: ",self.tail.data)
				print("LOG: List size: ",self.size) 

				temp = self.head
			
				while(temp!= None):
					print(temp.data,end = '')
					temp = temp.next
					print("-->",end = '')
				print(temp)
				print("LOG: End of list")
	
	
if __name__ == '__main__':
	Sllist = SinglyLinkedList()
	Sllist.print_choice()
	
		
