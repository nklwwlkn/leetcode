class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        combination = []

        hm = {
            "" : [""],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def backtrack(i, holder):
            if len(holder) == len(digits):
                res.append(holder)
                return
            
            for digit in hm[digits[i]]:
                combination.append(holder + digit)

                backtrack(i + 1, holder + digit)

                combination.pop()

        if digits:
            backtrack(0, "")

        return res
        