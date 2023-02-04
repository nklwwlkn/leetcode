class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        numStr = str(n)
        p = 1
        s = 0
        
        for i in range(len(numStr)):
            intStr = int(numStr[i])
            s += intStr
            p *= intStr
        
        return p - s
    


                