class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfiedAnyway = 0 
        maxExtraSatisfied = 0
        extraSatisfied = 0
        
        for i in range(len(customers)):
            if grumpy[i] == 0:
                satisfiedAnyway += customers[i]
            else:
                extraSatisfied += customers[i]

            if i >= minutes:
                if grumpy[i - minutes] == 1:
                    extraSatisfied -= customers[i - minutes]

            maxExtraSatisfied = max(maxExtraSatisfied, extraSatisfied)

        return satisfiedAnyway + maxExtraSatisfied
            