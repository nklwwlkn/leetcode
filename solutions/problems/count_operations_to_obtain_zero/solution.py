class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        counter = 0
        while num1 and num2:
            counter += max(num1, num2) // min(num1, num2)
            num1, num2 = num1 % num2, num2 % num1

        return counter