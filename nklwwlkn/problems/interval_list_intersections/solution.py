class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:   
        
        res = []
        i = 0
        j = 0
        while i < len(firstList) and j < len(secondList):
            startFirst, endFirst = firstList[i]
            startSecond, endSecond = secondList[j]

            if startFirst <= endSecond and startSecond <= endFirst:
                start = max(startFirst, startSecond)
                end = min(endFirst, endSecond)

                res.append([start, end])
                
            if endFirst < endSecond:
                i += 1
            else:
                j += 1

        return res
        
        
        