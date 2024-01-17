class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        n = len(matrix)
        
        result = []
        
        for i in range(n):
            temp = []
            for j in range(n):
                temp.append(matrix[n - j - 1][i])
                
            result.append(temp)
        
        for i in range(n):
            for j in range(n):
                matrix[i][j] = result[i][j]