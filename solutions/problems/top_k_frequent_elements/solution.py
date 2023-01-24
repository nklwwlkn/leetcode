class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, -1) + 1
        
        bucket = [[] for _ in range(len(nums))]

        for key in hmap:
            bucket[hmap.get(key)].append(key)

        mostFreq = []
        print(bucket)
        for i in range(len(bucket) -1, -1, -1):
            for num in bucket[i]:
                mostFreq.append(num)
            if len(mostFreq) == k:
                break
        
        return mostFreq
    




       


        