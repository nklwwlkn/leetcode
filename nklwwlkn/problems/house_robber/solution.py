class Solution:
    def rob(self, nums: List[int]) -> int:
        lastHouse = len(nums) - 1

        @cache
        def robHouse(house):
            if house == 0:
                return nums[0]
            if house == 1:
                return max(nums[0], nums[1])

            downOne = robHouse(house - 1)
            downTwo = robHouse(house - 2) + nums[house]

            return max(downOne, downTwo)
        
        return robHouse(lastHouse)
        