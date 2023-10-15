class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)

        for key, value in rCounter.items():
            if not key in mCounter or mCounter.get(key) < value:
                return False
        

        return True