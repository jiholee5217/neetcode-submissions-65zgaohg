# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # finds the middle algorithm (if even then slow.next is the ceiling of mid and if odd, slow.next is mid)
        slow = head 
        fast = head.next
        while fast and fast.next: # while fast is not Null and fast.next is not Null
            slow = slow.next # move slow by one
            fast = fast.next.next # move fast by two
        
        second = slow.next
        prev = slow.next = None
        # algorithm to reverse the second half of the list
        while second: # while second is not Null
            temp = second.next # store next node from second
            second.next = prev # set the next node to None on first loop otherwise set it to the node previous
            prev = second # prev is equal to second node 
            second = temp # second is not the next node from second
        
        first, second = head, prev # first is head of the list and second is equal to the last node of the
                                   # reversed second part of the list 
        while second: 
            tmp1, tmp2 = first.next, second.next #tmp1 = next of first list and tmp2 = next of second list
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            

