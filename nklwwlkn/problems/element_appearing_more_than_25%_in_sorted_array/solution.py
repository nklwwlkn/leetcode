class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr)

        candidates = [arr[size // 4], arr[size // 2], arr[3 * size // 4]]
        target = size / 4

        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1

            if right - left + 1 > target:
                return candidate

        return -1         