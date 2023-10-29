class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if not key in self.d:
            return res
        
        l, r = 0, len(self.d.get(key)) - 1

        while l <= r:
            m = l + (r - l) // 2

            if timestamp >= self.d[key][m][0]:
                res = self.d[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)