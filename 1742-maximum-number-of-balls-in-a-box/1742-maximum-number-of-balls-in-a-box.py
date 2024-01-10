class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        groups = [[] for _ in range(45)]
        result = 0
        
        for i in range(lowLimit, highLimit + 1):
            s = str(i)
            temp = 0
            for j in s:
                temp += int(j)
                
            # print(i, temp)
            groups[temp - 1].append(i)
            
        print(groups)
        
        max_length = 1
        
        for group in groups:
            max_length = max(len(group), max_length)
        
        return max_length