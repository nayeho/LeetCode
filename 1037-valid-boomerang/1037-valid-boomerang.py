class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        
        if points[0] == points[1] or points[1] == points[2] or points[2] == points[0]:
            return False
        
        x1 = points[0][0]
        y1 = points[0][1]
        x2 = points[1][0]
        y2 = points[1][1]
        x3 = points[2][0]
        y3 = points[2][1]
        
        dx1 = x2 - x1
        dy1 = y2 - y1
        
        dx2 = x3 - x2
        dy2 = y3 - y2
        
        if x1 == x2 and x2 == x3:
            return False
        
        if y1 == y2 and y2 == y3:
            return False
        
        if dx1 == 0 or dx2 == 0:
            return True
        
        if dy1 == 0 or dy2 == 0:
            return True
        
        m1 = dy1 / dx1
        m2 = dy2 / dx2
        
        return m1 != m2
        
               
               
               