class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        stack = []
        for char in num:
            while k and stack and int(stack[-1]) > int(char):
                stack.pop()
                k -= 1

            if stack or char != "0":
                stack.append(char)
        
        while k and stack:
            stack.pop()
            k -= 1

        return "".join(stack) if stack else "0"

        