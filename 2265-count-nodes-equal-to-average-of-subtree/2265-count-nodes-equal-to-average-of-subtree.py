# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        answer = 0

        def dfs(root: Optional[TreeNode]) -> Tuple[int, int]:
            nonlocal answer
            if not root:
                return (0, 0)

            leftSum, leftCount = dfs(root.left)
            rightSum, rightCount = dfs(root.right)
            summ = root.val + leftSum + rightSum
            count = 1 + leftCount + rightCount
            if summ // count == root.val:
                answer += 1
            return (summ, count)

        dfs(root)
        return answer
        