class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_len = len(nums)

        if nums_len == k:
            return nums
        
        bucket = [[] for i in range(nums_len)]
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, -1) + 1

        for key in hmap:
            bucket[hmap[key]].append(key)
        
        res = []

        print(bucket)
        
        i = len(bucket) - 1
        while len(res) != k:
            for elem in bucket[i]:
                res.append(elem)
            i -= 1

        return res

            
        