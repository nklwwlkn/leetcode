class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums
        
        frequency = {}
        bucket = [[] for i in range(len(nums) + 1)]
        res = []
        
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
     
        for n, c in frequency.items():
            bucket[c].append(n)
        
        for i in range((len(bucket) - 1), 0, -1):
            for n in bucket[i]:
                res.append(n)
            
            if len(res) == k:
                return res