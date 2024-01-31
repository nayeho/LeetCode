class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        
        result = 0
        s = set(nums)
        
        for num in s:
            if nums.count(num) == 1:
                result += num
                
        return result
        