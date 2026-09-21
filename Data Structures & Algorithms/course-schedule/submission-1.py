class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)] # prereq -> course
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            indegree[course] += 1 # course -> # of prereq

        queue = deque()
        completed = 0
        
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        while queue:
            course = queue.popleft()
            completed += 1

            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            

        return completed == numCourses
