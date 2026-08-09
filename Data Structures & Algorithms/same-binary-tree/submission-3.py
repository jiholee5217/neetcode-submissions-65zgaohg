# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None then return True
        if not p and not q:
            return True

        # if only one of them are None, return False because they are not the same
        if not p or not q:
            return False

        # if both values are not the same then we can also return False
        if p.val != q.val:
            return False



        # we can do a dfs search down each path recursively

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right, q.right)