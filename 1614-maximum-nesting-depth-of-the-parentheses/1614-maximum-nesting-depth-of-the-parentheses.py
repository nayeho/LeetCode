class Solution:
    def maxDepth(self, s: str) -> int:
        result = 0
        opened = 0

        for c in s:
            if c == '(':
                opened += 1
                result = max(result, opened)
            elif c == ')':
                opened -= 1

        return result
