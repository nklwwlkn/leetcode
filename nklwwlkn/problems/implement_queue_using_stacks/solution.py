class MyQueue:

    def __init__(self):
        self.stack_one = []
        self.stack_two = []
        

    def push(self, x: int) -> None:
        self.stack_one.append(x)

    def pop(self) -> int:
        self.peek()
        return self.stack_two.pop()
        

    def peek(self) -> int:
        if not self.stack_two:
            while self.stack_one:
                self.stack_two.append(self.stack_one.pop())

        return self.stack_two[-1]        

    def empty(self) -> bool:
        return len(self.stack_two) == 0 and len(self.stack_one) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()