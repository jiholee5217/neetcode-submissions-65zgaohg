"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copies = {}

        return self.dfs(node, copies)

    def dfs(self, node, copies):
        if node in copies:
            return copies[node]

        clone = Node(node.val)
        copies[node] = clone

        for neighbor in node.neighbors:
            clone.neighbors.append(self.dfs(neighbor, copies))
        
        return clone