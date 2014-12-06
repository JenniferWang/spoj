class Node():
	def __init__(self, val):
		self.val = val
		self.next = None

class SingleLinkedList(Node):
	def printList(self, head):
		pt = head
		while pt:
			print pt.val,
			pt = pt.next

	def quickSort(self, head, end):
		if not head or head == end:
			return

		pt = head
		pivot = end

		dummy = Node(0)
		dummy.next = head
		pt = head
		pt2 = dummy

		while pt != pivot:
			if pt.val > pivot.val:
				if not pivot.next:
					newEnd = pt
				tmp = pt.next
				pt.next = pivot.next
				pivot.next = pt
				pt2.next = tmp
				pt = pt2.next

			else:
				pt = pt.next
				pt2 = pt2.next

		if dummy.next != pivot:
			self.quickSort(head, pt2)

		if pivot.next:
			self.quickSort(pt.next, newEnd)
	
		
head = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
head.next = n1; n1.next = n2; n2.next = n3
sol = SingleLinkedList(head)
sol.printList(head)
sol.quickSort(head, n3)
sol.printList(head)

