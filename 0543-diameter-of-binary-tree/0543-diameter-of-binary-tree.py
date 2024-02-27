# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            nonlocal result
            if not root:
                return 0

            l = maxDepth(root.left)
            r = maxDepth(root.right)
            result = max(result, l + r)
            return 1 + max(l, r)

        maxDepth(root)
        return result