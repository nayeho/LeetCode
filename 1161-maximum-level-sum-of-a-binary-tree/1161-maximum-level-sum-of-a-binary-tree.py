# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        levelSums = []

        def dfs(root: Optional[TreeNode], level: int) -> None:
            if not root:
                return
            if len(levelSums) == level:
                levelSums.append(0)
            levelSums[level] += root.val
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        dfs(root, 0)

        return 1 + levelSums.index(max(levelSums))
        