class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)

        for num in arr:
            if c.get(num) > len(arr) / 4:
                return num
        