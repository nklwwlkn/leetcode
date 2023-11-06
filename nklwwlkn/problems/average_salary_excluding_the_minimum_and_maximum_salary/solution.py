class Solution:
    def average(self, salary: List[int]) -> float:
        maxSalary = float('-inf')
        minSalary = float('inf')
        total = 0

        for s in salary:
            if s > maxSalary:
                maxSalary = s

            if s < minSalary:
                minSalary = s
            
            total += s

        return (total - maxSalary - minSalary) / (len(salary) - 2)
             