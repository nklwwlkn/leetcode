class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxL = height[left]
        maxR = height[right]
        trapped = 0

        while left < right:
            if maxL < maxR:
                left += 1
                maxL = max(maxL, height[left])
                calc = maxL - height[left]
                if calc > 0:
                    trapped += calc
            else:
                right -= 1
                maxR = max(maxR, height[right])
                calc = maxR - height[right]
                if calc > 0:
                    trapped += calc

        return trapped
        