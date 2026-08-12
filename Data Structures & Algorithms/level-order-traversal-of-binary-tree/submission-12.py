# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None: # if tree is None then return an empty list
            return []

        res = [] # create a result list
        q = deque() # create a double ended queue
        q.append(root) # append the root to the queue
        while q: # run while queue is not empty
            level = [] # create a list for the current level
            n = len(q) # get the length of the current queue
            for i in range(n):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res



# 