class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        strNum = str(num)
        
        if len(strNum) == 1:
            return True
        
        return strNum[-1] != "0"