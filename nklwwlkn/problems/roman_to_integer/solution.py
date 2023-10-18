class Solution:
    def romanToInt(self, s: str) -> int:
        romanToInteger = { "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000 }
        res = 0

        for i in range(len(s)):
            integer = romanToInteger.get(s[i])
            nextt = romanToInteger.get(s[i + 1]) if i + 1 < len(s) else 0

            if integer < nextt:
                res -= integer
            else:
                res += integer

        return res
        