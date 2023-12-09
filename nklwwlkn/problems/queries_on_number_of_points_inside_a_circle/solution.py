class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        res = [0] * len(queries)

        for idx, query in enumerate(queries):
            xC, yC, rC = query

            rSquared = rC ** 2
            for xP, yP in points:
                dSquared = (xP - xC) ** 2 + (yP - yC) ** 2
                
                res[idx] += 1 if dSquared <= rSquared else 0

        return res
                
        