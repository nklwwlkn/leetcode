class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smaller = deque()
        larger = deque()
        equal = deque()

        for num in nums:
            if num < pivot:
                smaller.append(num)
            elif num > pivot:
                larger.append(num)
            else:
                equal.append(num)

        res = []
        while smaller:
            res.append(smaller.popleft())
        
        while equal:
            res.append(equal.popleft())
        
        while larger:
            res.append(larger.popleft())

        return res

        
        