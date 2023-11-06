class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        if s.isdigit():
            return ""
        
        for char in s:
            if char != "]":
                stack.append(char)
            else:
                tempStr = ""
                while stack[-1] != "[":
                    tempStr = stack.pop() + tempStr
                
                stack.pop()

                tempNum = ""
                while stack and stack[-1].isdigit():
                    tempNum = stack.pop() + tempNum

                stack.append(int(tempNum) * tempStr)

        return "".join(stack)
                