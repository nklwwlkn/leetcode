class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if len(arr) <= k:
            return max(arr)
       
        q = deque(arr[1:])
        wins = 0
        a = arr[0]

        while q:
            b = q.popleft()
            if a > b:
                wins += 1
                q.append(b)
            else:
                q.append(a)
                a = b
                wins = 1
            
            if wins == k:
                return a




        
        