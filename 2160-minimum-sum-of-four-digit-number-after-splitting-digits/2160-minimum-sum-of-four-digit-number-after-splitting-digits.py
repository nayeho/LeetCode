class Solution:
    def minimumSum(self, num: int) -> int:
        
        digit1 = num // 1000
        digit2 = num % 1000 // 100
        digit3 = num % 100 // 10
        digit4 = num % 10

        digits = [digit1, digit2, digit3, digit4]
        
        temp = []
        
        for i in range(4):
            d1 = i % 4
            d2 = (i + 1) % 4
            d3 = (i + 2) % 4
            d4 = (i + 3) % 4
            temp.append([digits[d1], digits[d2] * 100 + digits[d3] * 10 + digits[d4]])
            temp.append([digits[d1], digits[d2] * 100 + digits[d4] * 10 + digits[d3]])
            temp.append([digits[d1], digits[d3] * 100 + digits[d2] * 10 + digits[d4]])
            temp.append([digits[d1], digits[d3] * 100 + digits[d4] * 10 + digits[d2]])
            temp.append([digits[d1], digits[d4] * 100 + digits[d2] * 10 + digits[d3]])
            temp.append([digits[d1], digits[d4] * 100 + digits[d3] * 10 + digits[d2]])
            
            temp.append([digits[d2] * 100 + digits[d3] * 10 + digits[d4], digits[d1]])
            temp.append([digits[d2] * 100 + digits[d4] * 10 + digits[d3], digits[d1]])
            temp.append([digits[d3] * 100 + digits[d2] * 10 + digits[d4], digits[d1]])
            temp.append([digits[d3] * 100 + digits[d4] * 10 + digits[d2], digits[d1]])
            temp.append([digits[d4] * 100 + digits[d2] * 10 + digits[d3], digits[d1]])
            temp.append([digits[d4] * 100 + digits[d3] * 10 + digits[d2], digits[d1]])
            
        temp.append([digits[0] * 10 + digits[1], digits[2] * 10 + digits[3]])
        temp.append([digits[0] * 10 + digits[1], digits[3] * 10 + digits[2]])
        temp.append([digits[1] * 10 + digits[0], digits[2] * 10 + digits[3]])
        temp.append([digits[1] * 10 + digits[0], digits[3] * 10 + digits[2]])
        
        temp.append([digits[0] * 10 + digits[2], digits[1] * 10 + digits[3]])
        temp.append([digits[0] * 10 + digits[2], digits[3] * 10 + digits[1]])
        temp.append([digits[2] * 10 + digits[0], digits[1] * 10 + digits[3]])
        temp.append([digits[2] * 10 + digits[0], digits[3] * 10 + digits[1]])
        
        temp.append([digits[0] * 10 + digits[3], digits[1] * 10 + digits[2]])
        temp.append([digits[0] * 10 + digits[3], digits[2] * 10 + digits[1]])
        temp.append([digits[3] * 10 + digits[0], digits[1] * 10 + digits[2]])
        temp.append([digits[3] * 10 + digits[0], digits[2] * 10 + digits[1]])
        
            
        minVal = 1008
        for n1, n2 in temp:
            if n1 + n2 < minVal:
                minVal = n1 + n2
        
        return minVal
        