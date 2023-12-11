# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0, head)
        l = dummy
        r = head

        while r:
            for _ in range(m):
                if not r:
                    return dummy.next
                l = l.next
                r = r.next
            
            for _ in range(n):
                if not r:
                    break
                r = r.next
            
            l.next = r
            
        return dummy.next
        