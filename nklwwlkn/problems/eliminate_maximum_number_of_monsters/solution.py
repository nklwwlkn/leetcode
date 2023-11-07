class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = sorted([math.ceil(dist[i] / speed[i]) for i in range(len(dist))])

        count = 0
        for i in range(len(time)):
            if time[i] > i:
                count += 1 
            else:
                break
        
        return count
        