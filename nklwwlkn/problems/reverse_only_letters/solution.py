class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        chars = [*s]

        
        l = 0
        r = len(chars) - 1
        while l <= r:
            leftChar = chars[l]
            rightChar = chars[r]

            if not (65 <= ord(leftChar) <= 90 or 97 <= ord(leftChar) <= 122):
                l += 1
                continue

            if not (65 <= ord(rightChar) <= 90 or 97 <= ord(rightChar) <= 122):
                r -= 1
                continue
            
            self.swap(chars, l, r)
            l += 1
            r -= 1
        
        return "".join(chars)
    
    def swap(self, chars, l, r):
        chars[l], chars[r] = chars[r], chars[l]