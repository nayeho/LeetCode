# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = collections.deque([root])
        isEven = True

        while q:
            prevVal = -math.inf if isEven else math.inf
            sz = len(q)
            for _ in range(sz):
                node = q.popleft()
                if isEven and (node.val % 2 == 0 or node.val <= prevVal):
                    return False
                if not isEven and (node.val % 2 == 1 or node.val >= prevVal):
                    return False 
                prevVal = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            isEven = not isEven

        return True