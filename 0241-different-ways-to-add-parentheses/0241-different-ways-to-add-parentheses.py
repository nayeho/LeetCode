class Solution:
    @functools.lru_cache(None)
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []

        for i, c in enumerate(expression):
            if c in '+-*':
                for a in self.diffWaysToCompute(expression[:i]):
                    for b in self.diffWaysToCompute(expression[i + 1:]):
                        result.append(eval(str(a) + c + str(b)))

        return result or [int(expression)]