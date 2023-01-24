class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1


        while start < end:
            val_left = s[start].lower()
            val_right = s[end].lower()
    
            if not val_left.isalnum():
                start += 1
                continue
            if not val_right.isalnum():
                end -= 1
                continue

            if val_left != val_right:
                return False

            start += 1
            end -= 1

        return True
