class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        length = len(mat[0])
        for row in mat:
            for j in range(length):
                if row[j] != row[(j + k) % length]:
                    return False
        return True
        
        