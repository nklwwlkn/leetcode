class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        leftTime = max(left) if left else 0
        rightTime = max([n - pos for pos in right]) if right else 0

        return max(rightTime, leftTime)
    