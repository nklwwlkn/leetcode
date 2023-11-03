"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currToCopy = { None : None }

        curr = head
        while curr:
            currToCopy[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            copy = currToCopy[curr]
            copy.next = currToCopy[curr.next]
            copy.random = currToCopy[curr.random]

            curr = curr.next
        
        return currToCopy[head]