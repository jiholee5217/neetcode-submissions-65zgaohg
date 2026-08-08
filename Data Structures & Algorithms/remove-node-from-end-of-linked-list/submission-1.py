# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointers
        dummy = ListNode(0, head) # create a dummy node pointing to head
        left = dummy
        right = head

        while n > 0: # while n is greater than 0 and right is not None
            right = right.next # move right by 1
            n -= 1 # decrement n by 1

        while right: # while right is not None
            left = left.next # move left by 1
            right = right.next # move right by 1

        left.next = left.next.next
        return dummy.next

# first create a dummy node
# set two pointers, left to dummy and right to head
# while n is greater than zero and right is not None
# move right over by 1 and decrement n by 1
# while right is not None
# move left by 1 and right by 1
# now left should be right before the node to delete so set its next to left.next.next (leap over)
# return head by doing dummy.next
        


#       D
# d 1 2 3 4 N
#     l     r
# n = 0
