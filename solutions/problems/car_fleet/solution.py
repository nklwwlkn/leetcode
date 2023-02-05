class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleetCounter = 0
        currentTime = 0

        for pos, spd in sorted(pairs, reverse=True):
            destinationTime = (target - pos) / spd
            if destinationTime > currentTime:
                fleetCounter += 1
                currentTime = max(currentTime, destinationTime)

        
        return fleetCounter

