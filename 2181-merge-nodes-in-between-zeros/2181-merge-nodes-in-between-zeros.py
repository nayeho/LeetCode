# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next

        while curr:
            check = curr
            summ = 0
            while check.val:
                summ += check.val
                check = check.next

            curr.val = summ
            curr.next = check.next
            curr = check.next

        return head.next