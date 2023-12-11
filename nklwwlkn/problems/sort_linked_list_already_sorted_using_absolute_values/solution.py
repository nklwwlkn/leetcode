# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        r = head.next

        while r:
            if r.val < 0:
                l.next = r.next
                r.next = head 
                head = r
                r = l.next
            else:
                l = l.next
                r = r.next
          
        return head

            
        