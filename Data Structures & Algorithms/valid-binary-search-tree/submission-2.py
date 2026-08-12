# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minVal, maxVal):
            if node is None:
                return True
            if node.val >= maxVal or node.val <= minVal: 
                return False

            return isValid(node.left, minVal, node.val) and isValid(node.right, node.val, maxVal)
        
        return isValid(root, float('-inf'), float('inf'))