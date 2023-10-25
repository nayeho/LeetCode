# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None:
            return None
        
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if root.left is None:
                return root.right
            else:
                max_node = self.findMaxNode(root.left)
                
                root.val = max_node.val
                root.left = self.deleteNode(root.left, max_node.val)
            
        return root
    
    def findMaxNode(self, node):
        while node.right:
            node = node.right
        return node