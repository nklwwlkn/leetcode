class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums

        res = []

        bucket = [[] for i in range(len(nums) + 1)]
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 1) + 1
        
        for key in hmap:
            bucket[hmap.get(key) - 1].append(key)

        for i in range(len(bucket) -1, 0, -1):
            if len(res) == k:
                return res
            if len(bucket[i]) != 0:
                for elem in bucket[i]:
                    res.append(elem)

        return res
    
