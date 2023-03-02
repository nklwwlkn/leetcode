class TimeMap:

    def __init__(self):
        self.s = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.s[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        l, r = 0, len(self.s[key]) - 1

        while l <= r:
            m = (r - l) // 2 + l

            if self.s[key][m][1] <= timestamp:
                l = m + 1
                res = self.s[key][m][0]
            else:
                r = m - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)