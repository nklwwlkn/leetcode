class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        adjList = defaultdict(list)

        for fr, to in paths:
            adjList[fr].append(to)
        
        for fr, to in paths:
            if to not in adjList:
                return to