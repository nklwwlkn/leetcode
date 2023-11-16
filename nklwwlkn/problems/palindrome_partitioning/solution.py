class Solution:
    def isPalindrome(self, l, r, s):
        while l < r:
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def backtrack(j):
            if j >= len(s):
                res.append(partition.copy())
                return

            for i in range(j, len(s)):
                if self.isPalindrome(j, i, s):
                    partition.append(s[j : i + 1])

                    backtrack(i + 1)

                    partition.pop()
            
        
        backtrack(0)

        return res


        