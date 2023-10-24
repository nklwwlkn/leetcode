class Solution:
    def isValid(self, s: str) -> bool:
        closedToOpen = { "]" : "[", ")" : "(", "}" : "{"}
        stack = []

        for bracket in s:
            if bracket in closedToOpen:
                if stack and stack[-1] == closedToOpen.get(bracket):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
        
        return len(stack) == 0