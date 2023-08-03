from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        arr = []
        for i in range(n):
            arr.append(i + 1)
        
        return list(combinations(arr, k))
    
        