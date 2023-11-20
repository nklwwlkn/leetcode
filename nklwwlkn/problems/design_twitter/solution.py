class Twitter:

    def __init__(self):
        self.count = 0
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []

        self.followers[userId].add(userId)
        for subscribedId in self.followers[userId]:
            if subscribedId in self.tweets:
                index = len(self.tweets[subscribedId]) - 1
                count, tweetId = self.tweets[subscribedId][index]
                maxHeap.append((count, tweetId, subscribedId, index - 1))
        
        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            count, tweetId, subscribedId, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweets[subscribedId][index]
                heapq.heappush(maxHeap, (count, tweetId, subscribedId, index - 1))
            
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)