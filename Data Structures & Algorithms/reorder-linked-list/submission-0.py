# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dq = deque()
        cur = head

        if cur is None:
            return

        while cur is not None:
            dq.append(cur)
            cur = cur.next

        cur = head
        dq.popleft()

        alternating = True

        while dq:
            if alternating:
                cur.next = dq.pop()
            else:
                cur.next = dq.popleft()

            cur = cur.next
            alternating = not alternating

        cur.next = None
        return
        
