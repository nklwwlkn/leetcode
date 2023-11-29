# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        l = dummy
        r = head
        while r:
            if l.val > 0:
                gcdNode = ListNode(math.gcd(l.val, r.val))
                l.next = gcdNode
                gcdNode.next = r

                l = l.next.next
                r = r.next
            else:
                l = l.next
                r = r.next
        
        return dummy.next
        