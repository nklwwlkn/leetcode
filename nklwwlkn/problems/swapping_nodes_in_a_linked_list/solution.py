# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        l = head
        for _ in range(k - 1):
            l = l.next
        
        rLeft = head
        rRight = head
        for _ in range(k - 1):
            rRight = rRight.next
        
        while rRight.next:
            rLeft = rLeft.next
            rRight = rRight.next
        
        temp = l.val
        l.val = rLeft.val
        rLeft.val = temp

        return head
            
            