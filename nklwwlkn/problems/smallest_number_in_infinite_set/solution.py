class SmallestInfiniteSet:
    def __init__(self):
        self.smallest = 1
        self.minHeap = []
        self.addedBack = set()

    def popSmallest(self) -> int:
        if self.minHeap:
            smallest = heapq.heappop(self.minHeap)
            self.addedBack.remove(smallest)
            return smallest

        smallest = self.smallest
        self.smallest += 1
        return smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest and not num in self.addedBack: 
            heapq.heappush(self.minHeap, num)
            self.addedBack.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)