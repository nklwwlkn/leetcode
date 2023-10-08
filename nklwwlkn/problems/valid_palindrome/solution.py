class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l <= r:
            left = s[l].lower()
            right = s[r].lower()

            if not left.isalnum():
                l += 1
                continue
            if not right.isalnum():
                r -= 1
                continue

            if left != right:
                return False

            l += 1
            r -= 1

        return True