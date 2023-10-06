class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()

        
        def dfs(image, visited, r, c, color, newColor):
            if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visited or image[r][c] != color:
                return 
            
            visited.add((r,c))

            image[r][c] = newColor

            dfs(image, visited, r + 1, c, color, newColor)
            dfs(image, visited, r - 1, c, color, newColor)
            dfs(image, visited, r, c + 1, color, newColor)
            dfs(image, visited, r, c - 1, color, newColor)

            return image[r][c]

        dfs(image, visited, sr, sc, image[sr][sc], color)

        return image



        
        
                


        