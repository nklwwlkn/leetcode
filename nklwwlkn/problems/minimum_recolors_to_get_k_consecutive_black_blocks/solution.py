class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        whites = 0

        minRecolors = float('inf')
        l = 0
        for r in range(len(blocks)):
            if blocks[r] == "W": whites += 1

            while r - l + 1 > k:
                if blocks[l] == "W": whites -= 1

                l += 1
            
            if (r - l + 1) == k:
                minRecolors = min(minRecolors, whites) 
        
        return minRecolors