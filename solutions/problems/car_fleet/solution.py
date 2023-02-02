class Solution(object):
    def carFleet(self, target, position, speed):
        pairs = [(position[i], speed[i]) for i in range(len(position))]
        fleets = curtime = 0
        
        for dist, speed in sorted(pairs, reverse=True):
            destination_time = float((target - dist))/speed
            if curtime < destination_time:
                fleets += 1
                curtime = destination_time

        return fleets