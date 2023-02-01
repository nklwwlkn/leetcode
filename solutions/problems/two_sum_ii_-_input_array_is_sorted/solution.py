class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size = len(numbers)
        if size == 2:
            return [1, 2]
        
        left = 0
        right = size - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]
        