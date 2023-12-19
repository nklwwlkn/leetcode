class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        c = Counter()

        reps = 0
        currSum = 0
        maxSum = 0

        l = 0
        for r in range(len(nums)):
            c[nums[r]] += 1

            if c[nums[r]] > 1: reps += 1

            currSum += nums[r]

            while r - l + 1 > k or reps > 0:
                if c[nums[l]] > 1: reps -= 1

                c[nums[l]] -= 1

                currSum -= nums[l]

                l += 1

            if r - l + 1 == k and reps == 0:
               maxSum = max(maxSum, currSum)
        
        return maxSum

        