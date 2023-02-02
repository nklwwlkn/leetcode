class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}": "{", ")": "(", "]": "["}
        stack = []

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen.get(char):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
        