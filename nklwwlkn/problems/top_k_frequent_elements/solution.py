class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        res = []
        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, value in counter.items():
            bucket[value].append(key)
        
        
        for item in reversed(bucket):
            if item and k:
                for val in item:
                    if k > 0:
                        res.append(val)
                        k -= 1
                    else:
                        return res
        
        return res
           
            
        