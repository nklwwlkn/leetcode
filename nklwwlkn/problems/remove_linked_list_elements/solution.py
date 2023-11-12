# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head: return None
        
        dummy = ListNode(0, head)
        left = dummy
        right = head
    
        while right:
            if right.val == val:
                left.next = right.next
            else:
                left = left.next
    
            right = right.next

        return dummy.next
        

        