class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenn = 0
        

    def get(self, index: int) -> int:
        if index >= self.lenn:
            return -1
        
        cur = self.head
        for _ in range(index):
            cur = cur.next
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        new = Node(val)

        if not self.head:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new

        self.lenn += 1
        

    def addAtTail(self, val: int) -> None:
        new = Node(val)

        if not self.head:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new

        self.lenn += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.lenn:
            return
        elif index == self.lenn:
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next

            new = Node(val)
            new.next = cur.next
            cur.next = new

            self.lenn += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.lenn:
            return
        elif index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            for _ in range(index - 1):
                cur = cur.next
        
            cur.next = cur.next.next
            if index == self.lenn - 1:
                self.tail = cur

        self.lenn -= 1
        if self.lenn == 0:
            self.head = self.tail = None