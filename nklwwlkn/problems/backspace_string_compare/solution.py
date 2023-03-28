class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(word):
            stack = []
            for char in word:
                if char != "#":
                    stack.append(char)
                elif stack:
                    stack.pop()
            
            return "".join(stack)

        return build(s) == build(t)
        