class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            left_value = s[l].lower()
            right_value = s[r].lower()

            if not left_value.isalnum():
                l += 1
                continue
            if not right_value.isalnum():
                r -= 1
                continue
            
            if left_value != right_value:
                return False
            
            l += 1
            r -= 1
        
        return True

        