class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        result = 0
        area = [0] * len(matrix[0])

        def largestRectangleArea(heights: List[int]) -> int:
            result = 0
            stack = []

            for i in range(len(heights) + 1):
                while stack and (i == len(heights) or heights[stack[-1]] > heights[i]):
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1 if stack else i
                    result = max(result, h * w)
                stack.append(i)

            return result

        for row in matrix:
            for i, num in enumerate(row):
                area[i] = 0 if num == '0' else area[i] + 1
            result = max(result, largestRectangleArea(area))

        return result