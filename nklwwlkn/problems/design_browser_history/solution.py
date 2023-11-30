class ListNode:
    def __init__(self, val = None, prv = None, nxt = None):
        self.val = val
        self.prev = prv
        self.next = nxt

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        visited = ListNode(url)

        self.history.next = visited
        visited.prev = self.history

        self.history = self.history.next
        

    def back(self, steps: int) -> str:
        while self.history.prev and steps > 0:
            self.history = self.history.prev
            steps -= 1
        
        return self.history.val
        

    def forward(self, steps: int) -> str:
        while self.history.next and steps > 0:
            self.history = self.history.next
            steps -= 1
        
        return self.history.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)