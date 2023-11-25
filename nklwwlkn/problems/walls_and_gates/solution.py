class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        ROWS = len(rooms)
        COLS = len(rooms[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            for _ in range(len(q)):
                currentR, currentC = q.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    r = currentR + dr
                    c = currentC + dc

                    if 0 <= r < ROWS and 0 <= c < COLS and rooms[r][c] == 2147483647:
                        rooms[r][c] = rooms[currentR][currentC] + 1
                        q.append((r, c))