class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        currentTime = 0
        fleetCount = 0

        for pos, spd in sorted(pairs, reverse=True):
            destinationTime = (target - pos) / spd

            if destinationTime > currentTime:
                currentTime = destinationTime
                fleetCount += 1
            
        return fleetCount
        