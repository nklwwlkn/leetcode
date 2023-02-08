class Solution:
    def alternateDigitSum(self, n: int) -> int:
        strNum = str(n)
        res = 0
        c = 1

        for char in strNum:
            if c % 2 != 0:
                res += int(char)
                c += 1
            else:
                res -= int(char)
                c -= 1
        
        return res