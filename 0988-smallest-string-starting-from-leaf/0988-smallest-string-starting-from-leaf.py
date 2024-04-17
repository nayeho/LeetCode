# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.result = ''
        self.dfs(root, '')
        return self.result

    def dfs(self, root, path):
        if not root:
            return

        path += chr(root.val + ord('a'))

        if not root.left and not root.right:
            if not self.result or self.result > path[::-1]:
                self.result = path[::-1]

        self.dfs(root.left, path)
        self.dfs(root.right, path)
