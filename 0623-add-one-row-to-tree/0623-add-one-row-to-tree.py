# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newRoot = TreeNode(val)
            newRoot.left = root
            return newRoot

        d = 0
        q = [root]

        while q:
            d += 1
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if d == depth - 1:
                    cachedLeft = node.left
                    cachedRight = node.right
                    node.left = TreeNode(val)
                    node.right = TreeNode(val)
                    node.left.left = cachedLeft
                    node.right.right = cachedRight
            if d == depth - 1:
                break

        return root