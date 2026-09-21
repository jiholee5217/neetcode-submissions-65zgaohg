class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = set()
        visiting = set()

        for course, prereq in prerequisites:
            graph[course].append(prereq)

        for course in range(numCourses):
            if self.dfs(course, graph, visited, visiting) == False:
                return False
        return True

    
    def dfs(self, course, graph, visited, visiting):
        if course in visited:
            return True
        if course in visiting:
            return False

        visiting.add(course)

        for prereq in graph[course]:
            if self.dfs(prereq, graph, visited, visiting) == False:
                return False
            
        visited.add(course)
        visiting.remove(course)

        return True


