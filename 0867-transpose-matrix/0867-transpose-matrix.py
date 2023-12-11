class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        arr = [[0 for j in range(rows)] for i in range(cols)]
        
        for i in range(rows):
            for j in range(cols):
                arr[j][i] = matrix[i][j]
                
        
        return arr
        