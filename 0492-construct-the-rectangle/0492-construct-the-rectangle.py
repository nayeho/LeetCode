class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        
        L = 0
        W = 0
        diff = 0
        result = [area, 1]
        
        n = int(sqrt(area))
        
        for i in range(1, n + 1):
            W = i
            L = area // i
            if W * L == area:
                if L - W < result[0] - result[1]:
                    result = [L, W]
            
        return result