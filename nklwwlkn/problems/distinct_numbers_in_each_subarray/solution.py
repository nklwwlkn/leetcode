class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        intToCount = defaultdict(int)
        ans = []
        
        l = 0
        for r in range(len(nums)):
            intToCount[nums[r]] += 1

            if r - l + 1 > k:
                intToCount[nums[l]] -= 1

                if intToCount[nums[l]] == 0:
                    del intToCount[nums[l]]
                
                l += 1
            
            if r - l + 1 == k:
                ans.append(len(intToCount))

        return ans

        