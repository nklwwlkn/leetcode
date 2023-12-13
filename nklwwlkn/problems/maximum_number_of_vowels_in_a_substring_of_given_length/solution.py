class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])

        vowelsN = 0
        maxN = 0
        l = 0
        for r in range(len(s)):
            if s[r] in vowels: 
                vowelsN += 1

            while (r - l + 1) > k:
                if s[l] in vowels: vowelsN -= 1

                l += 1
            
            if (r - l + 1) == k:
                maxN = max(maxN, vowelsN)

        return maxN            

