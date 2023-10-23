class Solution:
    def maxArea(self, height: List[int]) -> int:
        trapped = 0
        l, r = 0, len(height) - 1

        while l <= r:
            if height[l] < height[r]:
                trapped = max(trapped, (r - l) * height[l])
                l += 1
            else:
                trapped = max(trapped, (r - l) * height[r])
                r -= 1
        
        return trapped
            
        