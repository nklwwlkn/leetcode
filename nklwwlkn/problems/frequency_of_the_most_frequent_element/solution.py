class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        total = 0
        l = 0
        currMaxFreq = 0
        for r in range(len(nums)):
            total += nums[r]

            while (total + k) < (nums[r] * (r - l + 1)):
                total -= nums[l]
                l += 1

            currMaxFreq = max(currMaxFreq, r - l + 1)

        return currMaxFreq
        