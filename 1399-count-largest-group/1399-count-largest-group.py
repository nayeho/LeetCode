class Solution:
    def countLargestGroup(self, n: int) -> int:
        
        groups = [[] for _ in range(36)]
        result = 0
        
        for i in range(1, n + 1):
            s = str(i)
            temp = 0
            for j in s:
                temp += int(j)
                
            print(i, temp)
            groups[temp - 1].append(i)
            
        print(groups)
        
        max_length = 1
        
        for group in groups:
            max_length = max(len(group), max_length)
            
        for group in groups:
            if len(group) == max_length:
                result += 1
        
        return result
        