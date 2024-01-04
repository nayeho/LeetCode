class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        result = ''
        
        while 1:
            if columnNumber > 26:
                if columnNumber % 26 != 0:
                    result += chr((columnNumber % 26) + 64)
                    columnNumber = columnNumber // 26
                else:
                    result += 'Z'
                    columnNumber = columnNumber // 26 - 1
                
            else:
                if columnNumber == 0:
                    result += 'Z'
                else:
                    result += chr(columnNumber + 64)
                break
            
        return result[::-1]
        