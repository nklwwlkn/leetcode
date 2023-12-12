class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        window = set()
        counter = 0

        l = 0
        for r in range(len(s)):
            while (r - l + 1) > k or s[r] in window:
                window.remove(s[l])
                l += 1
            
            window.add(s[r])

            if r - l + 1 == k:
                counter += 1


        return counter
        