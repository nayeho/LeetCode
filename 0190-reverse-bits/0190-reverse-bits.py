class Solution:
    def reverseBits(self, n: int) -> int:
        binary_str = (bin(n))[2:][::-1] 
        
        answer_str = binary_str + "0"*(32-len(binary_str))
        
        answer = int(answer_str, 2)
        return answer