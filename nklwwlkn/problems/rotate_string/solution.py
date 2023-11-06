class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return True if len(s) == len(goal) and s in goal+goal else False