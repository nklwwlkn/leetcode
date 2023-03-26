class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(word):
            bucket = []

            for char in word:
                if char != "#":
                    bucket.append(char)
                elif bucket:
                    bucket.pop()
            
            return ''.join(bucket)

        return build(s) == build(t)
        