class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        ROWS = len(image)
        COLS = len(image[0])

        visited = set()
        
        def dfs(image: List[List[int]], x: int, y: int, color: int, newColor: int, visited):
            if x < 0 or y < 0 or x == ROWS or y == COLS or (x,y) in visited or image[x][y] != color:
                return image

            visited.add((x,y))

            image[x][y] = newColor

            dfs(image, x + 1, y, color, newColor, visited)
            dfs(image, x - 1, y, color, newColor, visited)
            dfs(image, x, y + 1, color, newColor, visited)
            dfs(image, x, y - 1, color, newColor, visited)

        dfs(image, sr, sc, image[sr][sc], color, visited)

        return image
        