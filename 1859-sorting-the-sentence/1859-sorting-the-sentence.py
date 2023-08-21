class Solution:
    def sortSentence(self, s: str) -> str:
        
        s_list = s.split(' ')
        
        length = len(s_list)
        
        result = [0 for i in range(length)]
        
        for i in range(length):
            idx = int(s_list[i][-1]) - 1
            value = s_list[i][:-1]
            result[idx] = value
        
        return ' '.join(result)
        
        