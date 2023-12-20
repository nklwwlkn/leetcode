class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        r1 = m - 1
        r2 = n - 1
        for r in range(n + m - 1, -1, -1):
            if r2 < 0:
                break
            if r1 >= 0 and nums2[r2] < nums1[r1]:
                nums1[r] = nums1[r1]
                r1 -= 1
            else:
                nums1[r] = nums2[r2]
                r2 -= 1
            
             
            
        
            