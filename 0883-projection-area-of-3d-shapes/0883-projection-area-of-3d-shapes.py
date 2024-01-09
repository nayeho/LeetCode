class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        x = sum(max(row) for row in grid)
        y = sum(max(col) for col in zip(*grid))
        z = sum(a > 0 for row in grid for a in row)
        
        return x + y + z