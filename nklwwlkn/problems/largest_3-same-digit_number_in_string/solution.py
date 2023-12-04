class Solution:
    def largestGoodInteger(self, num: str) -> str:
        candidates = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

        for candidate in candidates:
            if candidate in num:
                return candidate
        
        return ""