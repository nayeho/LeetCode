class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        else:
            result = [1]
            pre = self.getRow(rowIndex - 1)
            
            for i in range(1, rowIndex):
                result.append(pre[i - 1] + pre[i])
                
            result.append(1)
                
            return result
                
        