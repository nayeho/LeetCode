class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        
        result = []
        
        for n in nums:
            if n % 2 == 0:
                result.insert(0, n)
            else:
                result.append(n)
                
        return result
            
        
        
        