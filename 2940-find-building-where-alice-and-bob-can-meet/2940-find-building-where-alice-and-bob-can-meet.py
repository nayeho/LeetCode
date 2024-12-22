from dataclasses import dataclass

@dataclass
class IndexedQuery:
    queryIndex: int
    a: int
    b: int

    def __iter__(self):
        yield self.queryIndex
        yield self.a
        yield self.b

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        result = [-1] * len(queries)
        stack = []

        heightsIndex = len(heights) - 1
        for queryIndex, a, b in sorted([IndexedQuery(i, min(a, b), max(a, b))
                                        for i, (a, b) in enumerate(queries)],
                                       key=lambda x: -x.b):
            if a == b or heights[a] < heights[b]:
                result[queryIndex] = b
            else:
                while heightsIndex > b:
                    while stack and heights[stack[-1]] <= heights[heightsIndex]:
                        stack.pop()
                    stack.append(heightsIndex)
                    heightsIndex -= 1
                j = self._lastGreater(stack, a, heights)
                if j != -1:
                    result[queryIndex] = stack[j]

        return result

    def _lastGreater(self, A: list[int], target: int, heights: list[int]):
        l = -1
        r = len(A) - 1
        while l < r:
            m = (l + r + 1) // 2
            if heights[A[m]] > heights[target]:
                l = m
            else:
                r = m - 1
        return l