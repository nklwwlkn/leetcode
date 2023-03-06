class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = deque()
        l = 0
        res = []
        for r in range(len(nums)):
            while deq and nums[r] > nums[deq[-1]]:
                deq.pop()
            deq.append(r)

            if l > deq[0]:
                deq.popleft()

            if r - l + 1 == k:
                res.append(nums[deq[0]])
                l += 1
        return res


        