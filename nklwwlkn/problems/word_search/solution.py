class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])

        visited = set()

        letterCounter = Counter(word)

        if letterCounter[word[0]] > letterCounter[word[-1]]:
            word = word[::-1]

        def dfs(r, c, wordIndex):
            if wordIndex >= len(word):
                return True

            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or board[r][c] != word[wordIndex]:
                return False

            visited.add((r,c))

            res = (
                dfs(r + 1, c, wordIndex + 1)
                or dfs(r, c + 1, wordIndex + 1)
                or dfs(r - 1, c, wordIndex + 1)
                or dfs(r, c - 1, wordIndex + 1)
            )

            visited.remove((r,c))

            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
    
        return False