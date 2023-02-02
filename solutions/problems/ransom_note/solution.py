class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = {}

        for char in magazine:
            hashMap[char] = hashMap.get(char, 0) + 1

        for char in ransomNote:
            if char in hashMap and hashMap.get(char, 0) > 0:
                hashMap[char] = hashMap.get(char) - 1
            else:
                return False
        
        return True