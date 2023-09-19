class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        list_mat = []
        cnt = 0
        
        for m in mat:
            temp = (cnt, m.count(1))
            list_mat.append(temp)
            cnt += 1
            
        s = sorted(list_mat, key = lambda x : (x[1], x[0]))
        result = []
        
        for i in range(k):
            result.append(s[i][0])
        
        return result
        
        
        