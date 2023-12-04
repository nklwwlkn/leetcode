class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            visited.add(room)
            
            for n in rooms[room]:
                if n not in visited:
                    dfs(n)


        dfs(0)

        return len(visited) == len(rooms)

        

            

            
            




        
        
    
        