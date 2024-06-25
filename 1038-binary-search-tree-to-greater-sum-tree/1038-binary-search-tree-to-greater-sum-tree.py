# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        prefix = 0
        
        def reversedInorder(node):
            nonlocal prefix
            if node is None:
                return
            
            reversedInorder(node.right)
            
            node.val += prefix
            prefix = node.val
            
            reversedInorder(node.left)
        
        reversedInorder(root)
        return root