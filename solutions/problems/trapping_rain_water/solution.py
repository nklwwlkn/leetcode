class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l = 0
        r = len(height) -1
        maxL = height[l]
        maxR = height[r]

        trapped = 0
        while l < r:
            if maxL < maxR: 
                l += 1
                maxL = max(maxL, height[l])
                calc = maxL - height[l]
                if calc >= 0:
                    trapped += calc
            else:
                r -= 1
                maxR = max(maxR, height[r])
                calc = maxR - height[r]
                if calc >= 0:
                    trapped += calc
        
        return trapped
            
