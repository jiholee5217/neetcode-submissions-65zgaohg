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
            for i in range(n): # loop the number equal to the length of the queue
                node = q.popleft() # get the first node in the queue
                level.append(node.val) # append it to level list
                if node.left: # if there is left node then append it to queue
                    q.append(node.left)
                if node.right: # if there is right node then append it to the queue
                    q.append(node.right)
            res.append(level) # append the level to the res list at the end

        return res



# 