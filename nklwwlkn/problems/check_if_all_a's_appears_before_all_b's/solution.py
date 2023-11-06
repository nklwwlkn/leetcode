class Solution:
    def checkString(self, s: str) -> bool:
        counter = Counter(s)
        count = 0

        for char in s:
            if char == "b":
                break
            if char == "a":
                count += 1
        
        return counter['a'] == count
            