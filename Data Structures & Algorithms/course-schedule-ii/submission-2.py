class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        visited = set()
        visiting = set()
        order = []
    
        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if self.dfs(course, graph, visited, visiting, order) == False:
                return []

        return order

    def dfs(self, course, graph, visited, visiting, order):
        if course in visited:
            return True
        if course in visiting:
            return False

        visiting.add(course)

        for prereq in graph[course]:
            if self.dfs(prereq, graph, visited, visiting, order) == False:
                return False

        visiting.remove(course)
        visited.add(course)

        order.append(course)

        return True