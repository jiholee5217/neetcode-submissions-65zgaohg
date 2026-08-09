# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None:
            return False
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, p, q):
        if not p and not q: # base case if both reach None then they are the same up to that point
            return True
        if not p or not q: # if one of them are None then return False
            return False
        if p.val != q.val: # if the value does not match for either node then return False
            return False
        
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)