class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = 0
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        for key in hm:
            if hm[key] > 1:
                # In the mathematical expression "NC2":
                # N refers to the total number of elements in a set,
                # and C2 refers to the number of ways to choose 2 elements from that set.
                counter += int(hm[key] * (hm[key] - 1) / 2)
        
        return counter
