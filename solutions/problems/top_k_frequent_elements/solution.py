class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        bucket = [[] for _ in range(len(nums))]
        res = []

        for num in count:
            bucket[count[num] - 1].append(num)

        for arr in reversed(bucket):
            if len(arr) and len(res) < k:
                for elem in arr:
                    res.append(elem)
        
        return res

       