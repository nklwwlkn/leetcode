class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topological = []
        visited = set()
        cycle = set()

        adjList = defaultdict(list)

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
            topological.append(course)

            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []

        return topological


        