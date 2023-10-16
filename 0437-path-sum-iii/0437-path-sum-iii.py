# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0
        
        def dfs(root, targetSum):
            result = 0
            if not root:
                return result
            if targetSum == root.val:
                result += 1
            result += dfs(root.left, targetSum - root.val)
            result += dfs(root.right, targetSum - root.val)
            return result
        
        return dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        
        