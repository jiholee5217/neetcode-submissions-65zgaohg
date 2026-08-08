# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle of the linkedlist
        slow, fast = head, head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = mid = slow.next
        # second reverse the second half of the list
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        head1 = head
        head2 = prev
        # work forward from first half and backword from second half and merge together into one list alternating
        while head1:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp
        return
