# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(head):
            if not head:
                return None
            
            head.next = dfs(head.next)

            return head.next if head.next and head.next.val > head.val else head
        
        return dfs(head)

        

        
        