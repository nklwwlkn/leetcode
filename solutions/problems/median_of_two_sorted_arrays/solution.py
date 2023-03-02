class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2
        a = nums1
        b = nums2

        if len(b) < len(a):
            a, b = b, a
        
        l, r = 0, len(a) - 1

        while True:
            midA = (r - l) // 2 + l
            midB = half - midA - 2

            aLeft = a[midA] if midA >= 0 else float('-inf')
            aRight = a[midA + 1] if midA + 1 < len(a) else float('inf')
            bLeft = b[midB] if midB >= 0 else float('-inf')
            bRight = b[midB + 1] if midB + 1 < len(b) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            else:
                if aLeft > bRight:
                    r = midA - 1
                else:
                    l = midA + 1
