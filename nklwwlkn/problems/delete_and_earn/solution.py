class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        hm = defaultdict(int)

        maxNum = 0
        for num in nums:
            hm[num] += num
            maxNum = max(maxNum, num)

        @cache
        def dp(i):
            if i == 0:
                return 0

            if i == 1:
                return hm[1]

            skip = dp(i - 1)
            earn = dp(i - 2) + hm[i]
            
            return max(skip, earn)

        return dp(maxNum)