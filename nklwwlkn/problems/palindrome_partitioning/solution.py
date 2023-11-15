class Solution:
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        substring = []

        def backtrack(j):
            if j >= len(s): 
                res.append(substring.copy())
                return

            for i in range(j ,len(s)):
                if self.isPalindrome(s, j, i):
                    substring.append(s[j : i + 1])
                    backtrack(i + 1)
                    substring.pop()

        backtrack(0)

        return res