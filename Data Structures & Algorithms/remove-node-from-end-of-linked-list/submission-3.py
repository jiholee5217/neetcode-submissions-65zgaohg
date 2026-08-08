# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers solution
        dummy = ListNode(0, head) # create a dummy node
        left = dummy # set left pointer to dummy 
        right = head # set right pointer to head

        while n > 0: # increment right pointer n times 
            right = right.next
            n -= 1

        while right: # now increment both left/right pointer until right is None
            left = left.next
            right = right.next

        # left pointer should not point to the node right before the nth node from end of the list so set
        # the left.next pointer to left.next.next and return dummy.next which points to the first node of the
        # linkedlist 
        left.next = left.next.next 
        return dummy.next