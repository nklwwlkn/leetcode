class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)
        visiting = set()
        visited  = set()
        res = []

        for course, prereq in prerequisites:
            adjList[course].append(prereq)

        
        def dfs(course):
            if course in visited:
                return True
            
            if course in visiting:
                return False
            
            visiting.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq):
                    return False
            
            visited.add(course)
            res.append(course)
        
            return True

        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return res