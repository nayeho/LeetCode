# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.dfs(root)
        return self.moves

    def dfs(self, node: TreeNode) -> int:
        if node is None:
            return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        self.moves += abs(left) + abs(right)
        
        return node.val - 1 + left + right