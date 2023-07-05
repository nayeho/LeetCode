class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        s_list = list(s)
        if numRows == 1:
            return s
        
        result_list = []
        for i in range(numRows):
            result_list.append([])

        idx = 0
        state = 'asc'
        for i in range(len(s_list)):
            
            if state == 'asc':
                result_list[idx].append(s_list[i])
                if idx != len(result_list) - 1:
                    idx += 1
                else:
                    state = 'desc'
                    idx -= 1
            else:
                result_list[idx].append(s_list[i])
                if idx != 0:
                    idx -= 1
                else:
                    state = 'asc'
                    idx += 1
        result = ''
        for i in range(len(result_list)):
            result += ''.join(result_list[i])

        return result
        