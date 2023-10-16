# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return head
        
        odd = head # 홀수 번째 노드를 모으는 리스트
        even = head.next # 짝수번째 노드를 모으는 리스트
        eHead = even # 마지막에 odd 뒤에 붙일 첫 번째 even의 주소
        
        while even and even.next:
        # even이 더 뒤에 위치하므로 even이 None이 아닌 범위 내에서만 반복한다.
        
            odd.next = odd.next.next
            even.next = even.next.next
            # 각 홀수/짝수 리스트의 next를 다음 홀수/짝수로 둔다.
            # 홀수 짝수를 한 덩어리로 묶어 진행하는 개념.
        
            odd = odd.next
            even = even.next
        
        odd.next = eHead # 홀수 리스트의 뒤에 짝수 리스트를 붙인다.
        
        return head 
        
        