class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1: return nums

        c = Counter(nums)
        bucket = [[] for _ in range(len(nums))]

        for num in c:
            bucket[c[num] - 1].append(num)

        print(bucket)
        
        res = []
        for arr in reversed(bucket):
            if arr and len(res) < k:
                for elem in arr:
                    if len(res) < k:
                        res.append(elem)

        return res

