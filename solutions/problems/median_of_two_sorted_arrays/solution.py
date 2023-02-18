class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            midA = (r - l) // 2 + l
            midB = half - midA - 2

            aLeft = A[midA] if midA >= 0 else float('-inf')
            aRight = A[midA + 1] if midA + 1 < len(A) else float('inf')
            bLeft = B[midB] if midB >= 0 else float('-inf')
            bRight = B[midB + 1] if midB + 1 < len(B) else float('inf')

            if aLeft <= bRight and bLeft <= aRight:
                if total % 2:
                    return min(aRight, bRight)
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight:
                r = midA - 1
            else:
                l = midA + 1
        