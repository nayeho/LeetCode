class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        result = 0

        for Ax, Ay in points:
            for Bx, By in points:
                for Cx, Cy in points:
                    result = max(result, 0.5 * abs((Bx - Ax) * (Cy - Ay) - (Cx - Ax) * (By - Ay)))

        return result