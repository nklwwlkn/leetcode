class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(b) < len(a):
            a, b = b, a

        l, r = 0, len(a) - 1 
        
        while True:
            aMid = (r - l) // 2 + l
            bMid = half - aMid - 2

            aLeft = a[aMid] if aMid >= 0 else float('-inf')
            aRight = a[aMid + 1] if aMid + 1 < len(a) else float('inf')
            bLeft = b[bMid] if bMid >= 0 else float('-inf')
            bRight = b[bMid + 1] if bMid + 1 < len(b) else float('inf') 

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            else:
                if aLeft > bRight:
                    r = aMid - 1
                else:
                    l = aMid + 1


        