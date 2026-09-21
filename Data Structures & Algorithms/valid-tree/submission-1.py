class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        if self.dfs(0, -1, graph, visited) == False:
            return False

        return len(visited) == n

    def dfs(self, node, parent, graph, visited):
        if node in visited:
            return False

        visited.add(node)

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            if self.dfs(neighbor, node, graph, visited) == False:
                return False
            
        return True