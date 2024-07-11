class Solution:
    def reverseParentheses(self, s: str) -> str:
        result = []
        stack = []
        check = {}

        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif c == ')':
                j = stack.pop()
                check[i] = j
                check[j] = i

        i = 0
        d = 1
        while i < len(s):
            if s[i] in '()':
                i = check[i]
                d = -d
            else:
                result.append(s[i])
            i += d

        return ''.join(result)