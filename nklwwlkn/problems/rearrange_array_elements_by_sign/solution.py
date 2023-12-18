class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        res = []

        for num in nums:
            if num > 0:
                pos.append(num)
            elif num < 0:
                neg.append(num)
        
        for p, n in zip(pos, neg):
            res += [p, n]
        
        return res
        
        
        