class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        c = Counter()

        res = 0
        l = 0
        for r in range(len(fruits)):
            c[fruits[r]] += 1

            while len(c) > 2:
                c[fruits[l]] -= 1
                if c[fruits[l]] == 0:
                    del c[fruits[l]]
                
                l += 1
            
            res = max(res, c.total())

        return res
