# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        maxPairSum = 0
        while prev:
            a = prev.val
            b = head.val

            maxPairSum = max(maxPairSum, a + b)

            prev = prev.next
            head = head.next
        
        return maxPairSum
        
        

        

    
        