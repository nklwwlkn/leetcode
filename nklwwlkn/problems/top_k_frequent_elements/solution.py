class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        counter = Counter(nums)
        res = []

        for num in counter:
            bucket[counter[num] - 1].append(num)

        for arr in reversed(bucket):
            if arr and len(res) < k:
                for num in arr:
                    if len(res) < k:
                        res.append(num)
        
        return res


        


        


        