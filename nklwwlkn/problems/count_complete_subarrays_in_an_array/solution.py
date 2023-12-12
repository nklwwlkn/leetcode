class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinctN = len(set(nums))
        intToCount = defaultdict(int)

        count = 0
        l = 0
        for r in range(len(nums)):
            intToCount[nums[r]] += 1

            while len(intToCount) == distinctN:
                count += len(nums) - r
                intToCount[nums[l]] -= 1

                if intToCount[nums[l]] == 0:
                    del intToCount[nums[l]]
                
                l += 1 

        return count
                
        