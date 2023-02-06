class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        diff = arr[-1] - arr[-2]

        for i in range(len(arr) - 2):
            if arr[i + 1] - arr[i] != diff:
                return False
            
        return True
