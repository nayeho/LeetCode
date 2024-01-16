from collections import Counter
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        
        temp = []
        
        for i in range(n):
            for j in range(n):
                temp.append(grid[i][j])
                
        c = Counter(temp).most_common()
        repeat = c[0][0]
        N = n * n
        S = N * (N + 1) // 2
        missing = S - (sum(temp) - repeat)
        
        return [repeat, missing]
        
        
        
            
        