class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def discoverBounds(idx, l, r):
            ll = idx
            resL = idx
            while ll >= l and nums[idx] == nums[ll]:
                resL = ll
                ll -= 1
            
            rr = idx
            resR = idx
            while rr <= r and nums[idx] == nums[rr]:
                resR = rr
                rr += 1
            
            return [resL, resR]
        
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l

            if nums[m] == target:
                return discoverBounds(m, l, r)
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1

        return [-1, -1]
        