from collections import deque
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positive_queue = deque()
        negative_queue = deque()
        result = []
        
        for num in nums:
            if num > 0:
                positive_queue.append(num)
            else:
                negative_queue.append(num)
                
        for _ in range(len(nums)//2):
            result.append(positive_queue.popleft())
            result.append(negative_queue.popleft())
            
        return result
            
        
        
        