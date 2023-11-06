class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        bucket = [0] * 5

        for char in text:
            if char == "b":
                bucket[0] += 1
            elif char == "a":
                bucket[1] += 1
            elif char == "l":
                bucket[2] += 1
            elif char == "o":
                bucket[3] += 1
            elif char == "n":
                bucket [4] += 1

        bucket[2] //= 2
        bucket[3] //= 2

        if bucket[2] == 0 or bucket[3] == 0:
            return 0
        
        minBaloons = min(bucket)

        return minBaloons
            