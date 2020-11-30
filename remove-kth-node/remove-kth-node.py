# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    pointer1 = head
	pointer2 = head
	count = 0
	while count < k:
		pointer2 = pointer2.next
		count += 1
	# if it is beyond the range, remove the first
	if pointer2 is None:
		head.value = head.next.value
		head.next = head.next.next
		return
	while pointer2.next is not None:
		pointer2 = pointer2.next
		pointer1 = pointer1.next
	pointer1.next = pointer1.next.next
