class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        duplicates = 1
        for char in s:
            if stack and stack[-1][0] == char:
                duplicates += 1
            else:
                duplicates = 1

            if duplicates == k:
                while stack and stack[-1][0] == char:
                    stack.pop()
                duplicates = stack[-1][1] if stack else 1
            else:
                stack.append((char, duplicates))
        

        return "".join([char for char, _ in stack])
            
    