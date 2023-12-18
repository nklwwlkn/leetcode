class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            for i in range(math.floor((len(row) + 1) / 2)):
                row[i], row[len(row) - 1 - i] = row[len(row) - 1 - i] ^ 1, row[i] ^ 1
        
        return image