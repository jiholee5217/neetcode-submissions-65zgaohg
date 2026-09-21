class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        num_components = 0

        for node in range(n):
            if node not in visited:
                num_components += 1
                self.dfs(node, graph, visited)
        return num_components

    def dfs(self, node, graph, visited):
        if node in visited:
            return

        visited.add(node)

        for neighbor in graph[node]:
            self.dfs(neighbor, graph, visited)