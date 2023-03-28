class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        q = deque([(0,0)])
        moves = 0
        offsets = [(2,1), (2, -1), (1, -2), (-1, -2), (1,2), (-1, 2), (-2, 1), (-2, -1)]
        visited = set([])

        while q:
            for _ in range(len(q)):
                current_x, current_y = q.popleft()

                if (current_x, current_y) == (x, y):
                    return moves

                for offset_x, offset_y in offsets:
                    next_x, next_y = current_x + offset_x, current_y + offset_y

                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
            moves += 1
        