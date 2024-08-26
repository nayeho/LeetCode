"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if root is None:
            return []

        result = []
        stack = [root]

        while stack:
            root = stack.pop()
            result.append(root.val)
            for child in root.children:
                stack.append(child)

        result.reverse()
        return result