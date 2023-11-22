class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False

        hs = set()

        l = 0
        for r in range(0, len(nums)):
            while (r - l) > k:
                hs.discard(nums[l])
                l += 1

            if nums[r] in hs:
                return True
            
            hs.add(nums[r])
    
        return False

        