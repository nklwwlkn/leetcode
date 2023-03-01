class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxAmount = 0

        while l < r:
            if height[l] < height[r]:
                maxAmount = max(maxAmount, (r - l) * height[l])
                l += 1
            else:
                maxAmount = max(maxAmount, (r - l) * height[r])
                r -= 1
        
        return maxAmount


        