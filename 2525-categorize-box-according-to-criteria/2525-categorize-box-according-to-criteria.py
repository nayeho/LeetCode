class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        
        isBulky = False
        isHeavy = False
        
        if max(length, width, height) >= 10**4 or length * width * height >= 10**9:
            isBulky = True
        
        if mass >= 100:
            isHeavy = True
            
        if isBulky and isHeavy:
            return 'Both'
        elif isBulky:
            return 'Bulky'
        elif isHeavy:
            return 'Heavy'
        else:
            return 'Neither'
        
        return None