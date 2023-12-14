class Solution:
    def minSwaps(self, data: List[int]) -> int:
        numberOfOnes = 0
        numberOfZeros = 0

        for binary in data: numberOfOnes += binary
        
        minSwaps = float('inf')
        l = 0 
        for r in range(len(data)):
            if data[r] == 0: numberOfZeros += 1

            while r - l + 1 > numberOfOnes:
                if data[l] == 0: numberOfZeros -= 1

                l += 1
            
            if r - l + 1 == numberOfOnes:
                minSwaps = min(minSwaps, numberOfZeros)
            
        
        return minSwaps
        