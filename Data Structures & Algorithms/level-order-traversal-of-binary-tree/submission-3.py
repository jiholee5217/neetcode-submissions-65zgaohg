# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()

        if root is None:
            return res
        else:
            q.append(root)

        while q:
            qlen = len(q)
            levels = []
            for i in range (qlen):
                node = q.popleft()
                levels.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(levels)

        return res