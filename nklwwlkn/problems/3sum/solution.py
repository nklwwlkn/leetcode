class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, z, p = [], [], []
        res = set()

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N, P = set(n), set(p)
        
        if len(z) >= 3:
            res.add(tuple([0, 0, 0]))
        
        if z:
            for num in P:
                if -num in N:
                    res.add(tuple(sorted([-num, 0, num])))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -(p[i] + p[j])

                if target in N:
                    res.add(tuple(sorted([target, p[i], p[j]])))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -(n[i] + n[j])

                if target in P:
                    res.add(tuple(sorted([target, n[i], n[j]])))

        return res
        