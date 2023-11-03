class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        hs = set(target)
        res = []
        for i in range(1, target[-1] + 1):
            if not i in hs:
                res.append("Push")
                res.append("Pop")
            else:
                res.append("Push")
        
        return res

        
        