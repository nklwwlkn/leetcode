class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        pairs = []        
        potions.sort()
        for idx, spell in enumerate(spells):
            pair = 0

            l = 0
            r = len(potions) - 1
            while l <= r:
                m = (r - l) // 2 + l

                if spell * potions[m] >= success:
                    r = m - 1
                else:
                    l = m + 1
            
            if l < len(potions):
                pairs.append(len(potions) - l)
            else:
                pairs.append(0)
        
        return pairs


        