class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            while l < r and nums[l] == nums[l + 1]:
                l += 1
            while r > l and nums[r] == nums[r - 1]:
                r -= 1

            m = (r - l) // 2 + l

            if nums[m] == target:
                return True

            elif nums[l] <= nums[m]: 
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                else: 
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1 
                else: 
                    r = m - 1

        return False
