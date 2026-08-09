# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None: # we could not find a sameTree as subRoot recursively and exhausted all options
            return False
        if self.sameTree(root, subRoot): # if root and subRoot are the sameTree then we met our condition so
                                         # we return true
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def sameTree(self, root, subRoot):
        if root is None and subRoot is None: # if both are none return true
            return True
        if root is None or subRoot is None: # if only of them are none return false
            return False
        if root.val != subRoot.val: # if values of root and subRoot does not match then return False
            return False

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)