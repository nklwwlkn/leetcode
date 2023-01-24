class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        size = len(matrix)
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        for r in range(size):
            for c in range(size):
                value = matrix[r][c]

                if value > size or value in rows[r] or value in cols[c]:
                    return False
                else:
                    rows[r].add(value)
                    cols[c].add(value)

        return True