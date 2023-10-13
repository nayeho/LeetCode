class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        
        length = len(grid)
        
        grid_T = []
        count = 0
        
        for i in range(length):
            temp = []            
            
            for j in range(length):
                temp.append(grid[j][i])
                
            grid_T.append(temp)
            
        for row in grid:
            for row_T in grid_T:
                if row == row_T:
                    count += 1
        
        return count
