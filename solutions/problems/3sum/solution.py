class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        z = []
        p = []
        n = []

        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)
            
        posSet = set(p)
        negSet = set(n)

        if z:
            for num in posSet:
                if -num in negSet:
                    res.add(tuple(sorted([num, -num, 0])))
        
        if len(z) >= 3:
            res.add(tuple([0,0,0]))

        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                val_i = p[i]
                val_j = p[j]
                target = -1 * (val_i + val_j)
                
                if target in negSet:
                    res.add(tuple(sorted([target, val_i, val_j])))
        
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                val_i = n[i]
                val_j = n[j]
                target = -1 * (val_i + val_j)
                
                if target in posSet:
                    res.add(tuple(sorted([target, val_i, val_j])))
        
        return res
            