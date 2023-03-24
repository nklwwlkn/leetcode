class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(2, -1), (2, 1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
       
        visited = set()
        q = deque([(0,0)])
        steps = 0
        while q:
            for _ in range(len(q)):
                current_x, current_y = q.popleft()

                if (current_x, current_y) == (x,y):
                    return steps

                for offset_x, offset_y in offsets:
                    next_x, next_y = offset_x + current_x, offset_y + current_y
                    if (next_x, next_y) not in visited:
                        visited.add((next_x, next_y))
                        q.append((next_x, next_y))
            steps += 1
        