class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsSize = len(nums)

        if numsSize == 1:
            return nums

        bucket = [[] for _ in range(numsSize)]
        hmap = {}
        res = []

        for num in nums:
            hmap[num] = hmap.get(num, -1) + 1

        for key in hmap:
            bucket[hmap[key]].append(key)

        for i in range(numsSize - 1, -1, -1):
            j = 0
            while len(res) != k and j < len(bucket[i]):
                res.append(bucket[i][j])
                j += 1
            
        
        return res
                


