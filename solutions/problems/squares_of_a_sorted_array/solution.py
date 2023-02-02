class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        stack = []

        while l <= r:
            if abs(nums[l]) >= nums[r]:
                stack.append(nums[l] ** 2)
                l += 1
            else:
                stack.append(nums[r] ** 2)
                r -= 1
            
        return reversed(stack)
                
