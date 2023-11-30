class Video:
    def __init__(self, content = None):
        self.content = content
        self.likes = 0
        self.dislikes = 0
        self.views = 0

class VideoSharingPlatform:

    def __init__(self):
        self.id = 0
        self.minIdHeap = []
        self.storage = defaultdict(Video)

    def upload(self, video: str) -> int:
        if self.minIdHeap:
            videoId = heapq.heappop(self.minIdHeap)
        else:
            videoId = self.id
            self.id += 1

            self.storage[videoId] = Video(video)

        return videoId

    def remove(self, videoId: int) -> None:
        if not videoId in self.storage:
            return None
        
        self.storage[videoId] = None
        heapq.heappush(self.minIdHeap, videoId)

    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if not videoId in self.storage:
            return "-1"
        
        video = self.storage[videoId]
        video.views += 1

        return video.content[startMinute : min(endMinute, len(video.content) - 1) + 1]        

    def like(self, videoId: int) -> None:
        if not videoId in self.storage:
            return
        
        self.storage[videoId].likes += 1
        

    def dislike(self, videoId: int) -> None:
        if not videoId in self.storage:
            return
        
        self.storage[videoId].dislikes += 1
        

    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if not videoId in self.storage:
            return [-1]

        video = self.storage[videoId]

        return [video.likes, video.dislikes]

    def getViews(self, videoId: int) -> int:
        if not videoId in self.storage:
            return -1

        video = self.storage[videoId]

        return video.views

        


# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)