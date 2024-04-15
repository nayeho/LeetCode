# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root: Optional[TreeNode], path: int) -> None:
            nonlocal result
            if not root:
                return
            if not root.left and not root.right:
                result += path * 10 + root.val
                return

            dfs(root.left, path * 10 + root.val)
            dfs(root.right, path * 10 + root.val)

        dfs(root, 0)
        return result