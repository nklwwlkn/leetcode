# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head

        prev = dummy
        curr = head.next
        gain = 0
        while curr:
            if curr.val != 0:
                gain += curr.val
            else:
                prev.val = gain
                gain = 0
                prev.next = curr if curr.next else None
                prev = prev.next

            curr = curr.next

        return dummy

        
        