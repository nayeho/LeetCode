class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        mem = [[[ -1 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        return self.cherry_pick(grid, 0, 0, n - 1, mem)
    
    def cherry_pick(self, grid: List[List[int]], x: int, y1: int, y2: int, mem: List[List[List[int]]]) -> int:
        if x == len(grid):
            return 0
        if y1 < 0 or y1 == len(grid[0]) or y2 < 0 or y2 == len(grid[0]):
            return 0
        if mem[x][y1][y2] != -1:
            return mem[x][y1][y2]
        
        curr_row = grid[x][y1] + (0 if y1 == y2 else 1) * grid[x][y2]
        
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                mem[x][y1][y2] = max(mem[x][y1][y2], curr_row + self.cherry_pick(grid, x + 1, y1 + d1, y2 + d2, mem))
        
        return mem[x][y1][y2]
