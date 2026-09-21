class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        visiting = set()
        visited = set()

        for course in range(numCourses):
            if not self.dfs(course, graph, visiting, visited):
                return False

        return True

    def dfs(self, course, graph, visiting, visited):
        if course in visited:
            return True
        if course in visiting:
            return False
        visiting.add(course)

        for prereq in graph[course]:
            if not self.dfs(prereq, graph, visiting, visited):
                return False

        visiting.remove(course)
        visited.add(course)
        return True