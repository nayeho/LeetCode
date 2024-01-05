class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        result = []
        
        H = [[], [], [], []]
        M = [[], [], [], [], [], []]
        
        H_POSSIBLE = [0, 1, 2, 3]
        M_POSSIBLE = [0, 1, 2, 3, 4, 5]
        
        POSSIBLE = [[], [], [], [], [], [], [], [], []]
        
        # POSSIBLE
        for i in range(len(H_POSSIBLE)):
            for j in range(len(M_POSSIBLE)):
                POSSIBLE[i + j].append((i, j))
                
        # H
        for i in range(12):
            temp = bin(i)[2:]
            cnt = list(temp).count('1')
            H[cnt].append(i)
        # print(H)        
        
        # M
        for i in range(60):
            temp = bin(i)[2:]
            cnt = list(temp).count('1')
            M[cnt].append(i)
        # print(M)
        
        if turnedOn > 8:
            return []
        
        for i, j in POSSIBLE[turnedOn]:
            list_H = H[i]
            list_M = M[j]
            
            for h in list_H:
                for m in list_M:
                    if len(str(m)) == 1:
                        result.append(str(h) + ':0' + str(m))
                    else:
                        result.append(str(h) + ':' + str(m))
        # print(result)
        return result
        