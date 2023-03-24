class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # remaining - string; pre_sum - int; pre_num - int
        def validate(remaining: str, pre_sum: int, pre_num: int):
            if len(remaining) == 0:
                return True
            if not remaining.startswith(str(pre_sum)):
                return False
            else:
                return validate(remaining[len(str(pre_sum)):], pre_sum + pre_num, pre_sum)
        
        # Iterate through num to get the first two numbers in this sequence
        for i in range(len(num) - 2):
            for j in range(i + 1, len(num) - 1):
                first = int(num[:i + 1])
                second = int(num[i + 1 : j + 1])
                # Continue if first or second has leading "0"
                if len(str(first)) != i + 1 or len(str(second)) != j - i:
                    continue
                if validate(num[j + 1:], first + second, second):
                    return True

        return False