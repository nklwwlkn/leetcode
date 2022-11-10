class Solution:
    def sanitize(self, s: str) -> str:
        res = ''
        for char in s:
            ord_char = ord(char)
            if ord_char >= 65 and ord_char <= 90:
                res += char.lower()
            elif ord_char >= 97 and ord_char <= 122:
                res += char
            elif ord_char >= 48 and ord_char <= 57:
                res += char
        
        return res
                
    
    def isPalindrome(self, s: str) -> bool:
        sanitized_s = self.sanitize(s)
        
        if len(sanitized_s) == 0:
            return True
        
        if len(sanitized_s) == 1:
            return True
        
        i = 0
        k = (len(sanitized_s) - 1)
        
        while i < k:
            if sanitized_s[i] != sanitized_s[k]:
                return False
            i += 1
            k -= 1
            
        return True
        