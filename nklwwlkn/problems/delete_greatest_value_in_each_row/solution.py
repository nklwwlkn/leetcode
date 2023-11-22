class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        minHeap = []
        
        for row in grid:
            row.sort()
        
        res = 0
        emptyRows = 0
        while emptyRows < len(grid):
            popped = []
            for row in grid:
                if row:
                    popped.append(row.pop())
                else:
                    emptyRows += 1

            if popped:
                res += max(popped)
        
        return res
                