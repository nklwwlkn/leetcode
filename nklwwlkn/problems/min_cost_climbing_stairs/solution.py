class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        topStair = len(cost)

        @cache
        def minCost(stair):
            if stair == 0:
              return 0
            
            if stair == 1:
              return 0

            downOne = cost[stair - 1] + minCost(stair - 1)
            downTwo = cost[stair - 2] + minCost(stair - 2)

            return min(downOne, downTwo)
        
        return minCost(topStair)
        