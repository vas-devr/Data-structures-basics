'''
This program is the Implemention of Non Dynamic Singly Linked List Data Structure. 
 
data : The value of the Node
next: pointer which points to next element of a node
head: pointer which points to first element of the node
tail: pointer which points to last element of the Node

Example:

|A| --> |B| -->|C|

head Pointer: points to A
tail Pointer : points to C
 again another test
 
 this is a test
'''

class Node:

	def __init__(self,data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	
	def __init__(self):
		self.head = None
		self.tail = None
		
	def printList(self):
		temp = self.head
		print("\nThe Singly Linked List Implementation\nThe Linked List has:")
		while(temp):
			print (temp.data)
			temp = temp.next
		print("The Head pointer:", self.head.data)
		print ("The Tail pointer:" ,self.tail.data)

if __name__ == '__main__':

	Sllist = SinglyLinkedList()
	Sllist.head = Sllist.tail = Node("A")
	second = Node("B")
	third = Node("C")
	
	Sllist.head.next = second
	second.next = third
	Sllist.tail = third
	Sllist.printList()
