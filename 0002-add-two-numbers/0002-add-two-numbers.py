# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Input : l1 = [2, 4, 3], l2 = [5, 6, 4]
        # Output : [7, 0, 8]
        result = ListNode() # dummy Node
        p = result # pointer
        carry = 0 # round up temp space
        
        while l1 or l2 or carry:
            sum = 0 # sum of each digit
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            sum = sum % 10
            
            p.next = ListNode(sum)
            p = p.next
        return result.next
        