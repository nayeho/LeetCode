class Solution:
    def arraySign(self, nums: List[int]) -> int:
        
        cnt_0 = nums.count(0)
        if cnt_0 > 0:
            return 0
        
        result = 1
        
        for num in nums:
            result *= 1 if num > 0 else -1
            
        return result
        