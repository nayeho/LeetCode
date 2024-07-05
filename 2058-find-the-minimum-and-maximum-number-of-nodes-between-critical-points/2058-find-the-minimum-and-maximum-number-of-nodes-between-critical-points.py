# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        prev = head
        curr = head.next
        
        check = math.inf
        idxFirst = -1
        idxPre = -1
        idx = 1

        while curr.next:
            if curr.val > prev.val and curr.val > curr.next.val or curr.val < prev.val and curr.val < curr.next.val:
                if idxFirst == -1:
                    idxFirst = idx
                if idxPre != -1:
                    check = min(check, idx - idxPre)
                idxPre = idx
            prev = curr
            curr = curr.next
            idx += 1

        if check == math.inf:
            return [-1, -1]
        return [check, idxPre - idxFirst]