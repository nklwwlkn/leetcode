# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        l = dummy
        r = list1

        while a:
            l = l.next
            r = r.next 
            a -= 1
            b -= 1
        
        while b:
            r = r.next
            b -= 1
        
        l.next = list2

        while list2.next:
            list2 = list2.next
        
        list2.next = r.next

        return dummy.next
        
        