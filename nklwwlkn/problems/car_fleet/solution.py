class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        grouped = [(position[i], speed[i]) for i in range(len(position))]
        fleetCounter = 0
        currTime = 0
        

        for pos, spd in sorted(grouped, reverse=True):
            destTime = (target - pos) / spd
            if destTime > currTime:
                currTime = max(currTime, destTime)
                fleetCounter += 1
        
        return fleetCounter

        
        