class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        index = 0
        count = 0

        for num in nums:
            if num < target:
                index += 1
            if num == target:
                count += 1
        
        return list(range(index, index + count))

    

