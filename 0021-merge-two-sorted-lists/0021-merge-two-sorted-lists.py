# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = ListNode(0) # dummy Node
        p = result # pointer
        temp = 0 # temporary
        
        if list1 == None:
            return list2
        
        if list2 == None:
            return list1
        
        while list1 != None and list2 != None:
            
            if list1.val < list2.val:
                temp = list1.val
                list1 = list1.next
            else:
                temp = list2.val
                list2 = list2.next
                
            p.next = ListNode(temp)
            p = p.next
            
        
        if list1 != None:
            p.next = list1
        else:
            p.next = list2
        
        return result.next
        