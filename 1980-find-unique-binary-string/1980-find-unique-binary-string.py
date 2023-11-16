class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        result = []
        answer = ''
        length = len(nums[0])
        low = 0
        high = 2 ** length - 1
        
        for num in nums:
            result.append(int(num, 2))
            
        for i in range(low, high + 1):
            if i not in result:
                answer = bin(i)[2:]
                
                if len(answer) == length:
                    return answer
                else:
                    return (length - len(answer))*'0' + answer
                
        
        return None