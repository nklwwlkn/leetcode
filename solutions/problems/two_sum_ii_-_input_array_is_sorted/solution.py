class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        k = len(numbers) - 1
        
        while numbers[k] + numbers[i] != target:
            s = numbers[k] + numbers[i]
            
            if s > target:
                k-= 1
            elif s < target:
                i+=1
            
        return [i + 1, k + 1]