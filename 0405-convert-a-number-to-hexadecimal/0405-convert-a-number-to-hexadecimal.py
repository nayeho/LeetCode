class Solution:
    def toHex(self, num: int) -> str:
        
        if num == 0:
            return '0'
        
        mp = '0123456789abcdef' # like a map
        result = ''
        
        for i in range(8):
            n = num & 15 # num & 1111b
            c = mp[n] # get the hex char
            result = c + result
            num = num >> 4
            
        return result.lstrip('0')
        