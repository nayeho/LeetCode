# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode()
        dummy.next = head
        
        p1 = dummy
        p2 = dummy
        
        for i in range(n + 1):
            p1 = p1.next
            
        while p1 != None:
            p1 = p1.next
            p2 = p2.next
            
        p2.next = p2.next.next
        
        return dummy.next
        