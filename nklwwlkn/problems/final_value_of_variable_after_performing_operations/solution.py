class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        counter = 0

        for o in operations:
            if o == "++X" or o == "X++":
                counter += 1
            elif o == "--X" or o == "X--":
                counter -= 1
            
        return counter