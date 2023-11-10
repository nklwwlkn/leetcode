class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        res = 0

        ts = 0
        fs = 0
        l = 0
        for r in range(len(answerKey)):
            if answerKey[r] == 'T':
                ts += 1
            else:
                fs += 1
            
            if (r - l + 1) - max(ts, fs) > k:
                if answerKey[l] == 'T':
                    ts -= 1
                else:
                    fs -= 1
                l += 1
        
            res = max(res, r - l + 1)
        
        return res

        