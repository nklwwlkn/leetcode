class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        cycle = set()
        visited = set()

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        def dfs(course):
            if course in visited:
                return True
            
            if course in cycle:
                return False
            
            cycle.add(course)
            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False

            visited.add(course)

            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True