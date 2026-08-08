# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # first find the middle
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next

        # reverse the back half of the linked list
        prev = None
        curr = mid

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev

        # merge the two together
        head1 = head
        head2 = curr

        while head1:
            temp = head1.next
            head1.next = head2
            head1 = head2
            head2 = temp

        return

