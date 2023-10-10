class Solution:
    def longestPalindrome(self, s: str) -> int:
        hm = dict()
        length = 0
        hasOdd = False

        for char in s:
            hm[char] = hm.get(char, 0) + 1

        for count in hm.values():
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                hasOdd = True
        
        return length + 1 if hasOdd else length

            
        