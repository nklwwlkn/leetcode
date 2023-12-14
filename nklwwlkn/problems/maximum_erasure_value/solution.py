class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        intToCount = defaultdict(int)
        reps = 0
        score = 0
        maxScore = 0

        l = 0
        for r in range(len(nums)):
            intToCount[nums[r]] += 1
            score += nums[r]

            if intToCount[nums[r]] > 1: reps += 1

            while reps > 0:
                score -= nums[l]
                intToCount[nums[l]] -= 1
                
                if intToCount[nums[l]] == 1: reps -= 1
                
                l += 1
            
            if reps == 0:
                maxScore = max(maxScore, score)

        return maxScore
        