Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        output = ListNode(0)
        tail = output
        carry = 0
        while l1 or l2 or carry:
            if l1:
                l1_val = l1.val
                l1 = l1.next
            else:
                l1_val = 0
            if l2:
                l2_val = l2.val
                l2 = l2.next
            else:
                l2_val = 0
            value = l1_val + l2_val + carry
            final_val = value % 10
            carry = int(value/10)
            tail.next = ListNode(final_val)
            tail = tail.next
           
        return output.next
                
                
            
            
        