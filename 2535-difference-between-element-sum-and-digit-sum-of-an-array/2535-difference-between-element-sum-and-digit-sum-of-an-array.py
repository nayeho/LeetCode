class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        
        sum_of_nums = 0
        sum_of_digits = 0
        
        for i in range(len(nums)):
            sum_of_nums += nums[i]
            
            digit1000 = nums[i] // 1000
            digit100 = nums[i] % 1000 // 100
            digit10 = nums[i] % 100 // 10
            digit1 = nums[i] % 10
            
            sum_of_digits += digit1000 + digit100 + digit10 + digit1
            
        return abs(sum_of_nums - sum_of_digits)
        