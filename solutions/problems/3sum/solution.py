class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        z = []
        p = []
        n = []
        res = set()

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        P = set(p)
        N = set(n)

        if len(z) >= 3:
            res.add(tuple([0,0,0]))

        if z:
            for num in P:
                if -num in N:
                    res.add(tuple(sorted([-num, 0, num])))
        
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))
        
        return res
                




        