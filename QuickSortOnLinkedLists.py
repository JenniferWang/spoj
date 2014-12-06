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
		print 'none'

	def partition(self, head, end):
		if not head or head == end:
			return None

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
		head = dummy.next
		self.printList(head)
		print pt2.val
		print pt.val
		return pivot

	def quickSort(self, head, end):
		pivot = self.partition(head, end)
		if not pivot:
			return
		if prePivot.next != head:
			self.quickSort(head, prePivot)
		if prePivot.next and prePivot.next.next:
			self.quickSort(prePivot.next.next, end)

		
head = Node(9)
n1 = Node(8)
n2 = Node(7)
n3 = Node(3)
head.next = n1; n1.next = n2; n2.next = n3
sol = SingleLinkedList(head)
sol.printList(head)
print
sol.partition(head, n3)

#sol.quickSort(head, n3)


