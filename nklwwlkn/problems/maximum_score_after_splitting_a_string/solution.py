class Solution:
    def maxScore(self, s: str) -> int:
        c = Counter(s)

        res = 0
        zeros = 0
        ones = 0
        for i in range(len(s) - 1):
            char = s[i]
            if char == "0": zeros += 1
            if char == "1": ones += 1

            res = max(res, zeros + c["1"]  - ones)                

        return res