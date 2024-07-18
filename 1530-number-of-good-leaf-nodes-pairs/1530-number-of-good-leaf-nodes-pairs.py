# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:

        result = 0

        def dfs(root, distance):
            nonlocal result
            d = [0] * (distance + 1)
            if root is None:
                return d
            if root.left is None and root.right is None:
                d[0] = 1
                return d

            dl = dfs(root.left, distance)
            dr = dfs(root.right, distance)

            for i in range(distance):
                for j in range(distance):
                    if i + j + 2 <= distance:
                        result += dl[i] * dr[j]

            for i in range(distance):
                d[i + 1] = dl[i] + dr[i]

            return d

        dfs(root, distance)
        return result