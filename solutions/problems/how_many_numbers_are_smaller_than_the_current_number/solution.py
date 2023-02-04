class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        possible_numbers = [0] * 101
        for num in nums:
            possible_numbers[num] += 1
        
        # Keep track prev count!
        for i in range(1, len(possible_numbers)):
            possible_numbers[i] = possible_numbers[i - 1] + possible_numbers[i]

        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = 0
            else:
                nums[i] = possible_numbers[num -1]

        return nums        




        