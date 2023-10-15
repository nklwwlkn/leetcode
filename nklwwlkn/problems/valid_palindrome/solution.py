class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            leftChar = s[l].lower()
            rightChar = s[r].lower()

            if not leftChar.isalnum():
                l += 1
                continue
            
            if not rightChar.isalnum():
                r -= 1
                continue
            
            if leftChar != rightChar:
                return False

            l += 1
            r -= 1

        return True