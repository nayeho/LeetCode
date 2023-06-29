class Solution:
    
    dic_tri = {'0':0, '1':1, '2':1}
    
    def tribonacci(self, n: int) -> int:
        
        if n < 3:
            return self.dic_tri[str(n)]
        else:
            
            for i in range(3, n + 1):
            
                temp = self.dic_tri[str(i - 1)] + self.dic_tri[str(i - 2)] + self.dic_tri[str(i - 3)]
                self.dic_tri[str(i)] = temp
        
        return self.dic_tri[str(n)]
        