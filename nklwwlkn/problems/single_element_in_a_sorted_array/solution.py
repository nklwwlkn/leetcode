class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def isSingleElement(idx):
            isLeftUnique = (idx == 0) or (nums[idx] != nums[idx - 1])
            isRightUnique = (idx == len(nums) - 1) or (nums[idx] != nums[idx + 1])

            return isLeftUnique and isRightUnique
         
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (r - l) // 2 + l

            if isSingleElement(m):
                return nums[m]
            
            if m % 2 == 0:
                if nums[m] == nums[m + 1]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if nums[m] == nums[m + 1]:
                    r = m - 1
                else:
                    l = m + 1
        
        return - 1

        