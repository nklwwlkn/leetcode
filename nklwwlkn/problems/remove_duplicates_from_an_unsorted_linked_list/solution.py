# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, None)
        newList = dummy 
        valToCount = dict()

        curr = head
        while curr:
            valToCount[curr.val] = valToCount.get(curr.val, 0) + 1
            curr = curr.next
        
        curr = head
        while curr:
            if valToCount[curr.val] == 1:
                newList.next = ListNode(curr.val)
                newList = newList.next
            
            curr = curr.next
        
        return dummy.next
        

        