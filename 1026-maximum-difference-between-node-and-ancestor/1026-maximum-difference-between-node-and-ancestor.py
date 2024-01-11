# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        return self.maxAncestorDiff2(root, root.val, root.val)
    
    def maxAncestorDiff2(self, root: Optional[TreeNode], minVal: int, maxVal: int) -> int:
        
        if not root:
            return 0
        
        minVal = min(minVal, root.val)
        maxVal = max(maxVal, root.val)
        
        l = self.maxAncestorDiff2(root.left, minVal, maxVal)
        r = self.maxAncestorDiff2(root.right, minVal, maxVal)
        
        return max(maxVal - minVal, max(l, r))