class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'

        result = []
        stack = []

        for i, digit in enumerate(num):
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        for _ in range(k):
            stack.pop()

        for c in stack:
            if c == '0' and not result:
                continue
            result.append(c)

        return ''.join(result) if result else '0'