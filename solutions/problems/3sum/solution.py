class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        p = []
        n = []
        z = []
        res = set()

        for num in nums:
            if num == 0:
                z.append(num)
            elif num > 0:
                p.append(num)
            else:
                n.append(num)
        
        P = set(p)
        N = set(n)

        if len(z) >= 3:
            res.add((0,0,0))
        
        if len(z) > 0:
            for num in P:
                if -num in N:
                    res.add((-num, 0, num))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([target, p[i], p[j]])))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([target, n[i], n[j]])))

        return res