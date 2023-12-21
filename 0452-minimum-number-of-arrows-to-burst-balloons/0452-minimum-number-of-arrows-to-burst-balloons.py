class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        result = 0
        arrowX = -math.inf
        
        points = sorted(points, key=lambda x: x[1])

        for point in points:
            if point[0] > arrowX:
                result += 1
                arrowX = point[1]

        return result