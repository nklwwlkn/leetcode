class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL = height[l]
        maxR = height[r]

        trapped = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                trapped += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                trapped += maxR - height[r]

        return trapped
