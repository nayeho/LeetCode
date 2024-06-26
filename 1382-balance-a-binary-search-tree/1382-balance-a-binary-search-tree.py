# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums = []

        def inorder(root: Optional[TreeNode]) -> None:
            if not root:
                return
            inorder(root.left)
            nums.append(root.val)
            inorder(root.right)

        inorder(root)

        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            m = (l + r) // 2
            return TreeNode(nums[m], build(l, m - 1), build(m + 1, r))

        return build(0, len(nums) - 1)