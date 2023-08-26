class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()

        for num in nums:
            d[num] = d.get(num, 0) + 1
            if d.get(num) >= 2:
                return True

        return False
