class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])
        
        
        for i in range(m):
            if target <= matrix[i][-1] :
                for j in range(n):
                    if target == matrix[i][j]:
                        return True
                    elif target < matrix[i][j]:
                        return False
                return False
                    
                
                
        