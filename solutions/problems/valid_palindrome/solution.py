class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            val_left = s[left].lower()
            val_right = s[right].lower()

            if not val_left.isalnum():
                left += 1
                continue
            if not val_right.isalnum():
                right -= 1
                continue
            
            if val_left != val_right:
                return False
            
            left += 1
            right -= 1

        return True
        