class SparseVector:
    def __init__(self, nums: List[int]):
        self.hm = {}
        
        for idx, num in enumerate(nums):
            if num != 0:
                self.hm[idx] = num
        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0

        if len(vec.hm) < len(self.hm):
            for key in vec.hm.keys():
                if key in self.hm:
                    res += self.hm[key] * vec.hm[key]
        else:
            for key in self.hm.keys():
                if key in vec.hm:
                    res += self.hm[key] * vec.hm[key]
        
        return res

        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)