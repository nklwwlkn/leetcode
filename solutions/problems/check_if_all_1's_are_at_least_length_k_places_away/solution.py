class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        lastPosition = -1 * k - 1
        for index, num in enumerate(nums):
            if num == 1:
                if index - lastPosition <= k:
                    return False
                else:
                    lastPosition = index
        return True


            
            