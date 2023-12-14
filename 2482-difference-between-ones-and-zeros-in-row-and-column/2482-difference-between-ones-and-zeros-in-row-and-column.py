class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        diff = [[0 for j in range(cols)] for i in range(rows)]
        onesRow = [grid[i].count(1) for i in range(rows)]
        zerosRow = [grid[i].count(0) for i in range(rows)]
        
        grid_T = self.transpose(grid)
        
        onesCol = [grid_T[j].count(1) for j in range(cols)]
        zerosCol = [grid_T[j].count(0) for j in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                
                diff[i][j] = onesRow[i] + onesCol[j] - zerosRow[i] - zerosCol[j]
        
        return diff
    
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        rows = len(matrix)
        cols = len(matrix[0])

        arr = [[0 for j in range(rows)] for i in range(cols)]

        for i in range(rows):
            for j in range(cols):
                arr[j][i] = matrix[i][j]

        return arr