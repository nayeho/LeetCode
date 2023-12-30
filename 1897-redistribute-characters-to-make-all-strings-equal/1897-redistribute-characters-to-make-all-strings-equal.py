from collections import Counter
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        m = len(words)
        
        temp = []
        for i in range(m):
            for j in range(len(words[i])):
                temp.append(words[i][j])
                
        # print(temp)
        c = Counter(temp).most_common()
        # print(c)
        
        for _, i in c:
            if i % m != 0:
                return False
        
        return True
        