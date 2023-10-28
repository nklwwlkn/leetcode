class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]

        fleets, currTime = 0, 0

        for pos, spd in sorted(pairs, reverse=True):
            destTime = (target - pos) / spd

            if destTime > currTime:
                fleets += 1
                currTime = destTime
        
        return fleets