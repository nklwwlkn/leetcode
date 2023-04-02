class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l, r = 0, len(self.d[key]) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if self.d[key][m][0] <= timestamp:
                res = self.d[key][m][1]
                l = m + 1
            else:
                r = m - 1
        
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)