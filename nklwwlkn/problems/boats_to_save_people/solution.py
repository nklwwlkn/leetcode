class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        boats = 0

        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
                boats += 1
            elif people[r] <= limit:
                r -= 1
                boats += 1
            
        return boats


            
        