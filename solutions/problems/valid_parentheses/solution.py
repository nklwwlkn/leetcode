class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {"}" : "{", ")" : "(", "]" : "[" }
        stack = []

        for bracket in s:
            if bracket in closeToOpen:
                if stack and stack[-1] == closeToOpen.get(bracket):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)
            
        
        return len(stack) == 0


        