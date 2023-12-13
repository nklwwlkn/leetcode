class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        ROWS = len(mat)
        COLS = len(mat[0])

        rows = defaultdict(int)
        cols = defaultdict(int)

        counter = 0
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                   rows[r] += 1
                   cols[c] += 1
        
    
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 1:
                   counter += 1 if rows[r] == cols[c] == 1 else 0
        
        return counter 
                       
        