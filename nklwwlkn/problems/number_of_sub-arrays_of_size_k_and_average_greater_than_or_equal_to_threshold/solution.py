class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        counter = 0
        
        summ = 0
        l = 0
        for r in range(len(arr)):
            summ += arr[r]
            while (r - l + 1) > k:
                summ -= arr[l]
                l += 1 
            
            if (summ / k) >= threshold and (r - l + 1) == k: counter += 1

        return counter
        