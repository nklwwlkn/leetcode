class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS = len(img)
        COLS = len(img[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        newImage = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                total = img[r][c]
                count = 1
                for directionR, directionC in directions:
                    currR = r + directionR
                    currC = c + directionC

                    if 0 <= currR < ROWS and 0 <= currC < COLS:
                        count += 1
                        total += img[currR][currC]
                
                newImage[r][c] = math.floor(total / count)
                
        
        return newImage