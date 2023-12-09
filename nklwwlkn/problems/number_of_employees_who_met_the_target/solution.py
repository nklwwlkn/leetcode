class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        counter = 0
        for hour in hours:
            if hour >= target:
                counter += 1

        return counter
        