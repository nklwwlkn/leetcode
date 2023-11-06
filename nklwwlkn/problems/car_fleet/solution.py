class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = [(position[i], speed[i]) for i in range(len(position))]
        fleets = 0
        currTime = 0

        for pos, spd in sorted(stack, reverse=True):
            destTime = (target - pos) / spd
            if destTime > currTime:
                fleets += 1
                currTime = max(currTime, destTime)
            
        return fleets