# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        result = []
        queue = collections.deque([root])
        
        while queue:
            largest = -float('inf')
            length = len(queue)
            for _ in range(length):
                
                node = queue.popleft()
                if node.val > largest:
                    largest = node.val
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
                    
            result.append(largest)
        return result
        