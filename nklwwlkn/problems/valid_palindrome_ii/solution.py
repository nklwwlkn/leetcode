class Solution:
    def validPalindrome(self, s: str) -> bool:
        canDelete = True

        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                deleteLeft = self.isPalindrome(s, l + 1, r)
                deleteRight = self.isPalindrome(s, l, r - 1)
                
                if not deleteLeft and not deleteRight:
                    return False
                
                return True
            
            l += 1
            r -= 1

        return True
    
    def isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            
            l += 1
            r -= 1
        
        return True