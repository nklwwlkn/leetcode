class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        taskToCount = Counter(tasks)
        maxHeap = [-count for count in taskToCount.values()]
        heapq.heapify(maxHeap)
        q = deque()

        time = 0
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                countLeft = heapq.heappop(maxHeap) + 1
                if countLeft:
                    q.append((countLeft, time + n))
            
            if q and time == q[0][1]:
                heapq.heappush(maxHeap, q.popleft()[0])


        return time
        