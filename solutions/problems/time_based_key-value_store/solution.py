class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value, timestamp])        
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.s[key]) - 1
        value = ""

        while l <= r:
            m = (r - l) // 2 + l

            if timestamp >= self.s[key][m][1]:
                l = m + 1
                value = self.s[key][m][0]
            else:
                r = m - 1
        
        return value


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)