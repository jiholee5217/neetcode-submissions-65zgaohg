# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the algorithm works like this:
        # if both p.value and q.value is less than current node then traverse to the left child
        # if both p.value and q.value is greater than current node then traverse to the right child
        # otherwise return current node
        # this all works because the given root is a binary search tree with no duplicates and not None
        curr = root
        while curr:
            if p.val < curr.val and q.val < curr.val:
                curr = curr.left
                self.lowestCommonAncestor(curr, p, q)
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
                self.lowestCommonAncestor(curr, p, q)
            else:
                return curr
