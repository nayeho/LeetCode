class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        length = len(nums)
        
        count_zero = nums.count(0)
        count_one = length - count_zero
        
        if count_zero == 0:
            return length - 1
        
        if count_one == 0:
            return 0
        
        s = ''.join(map(str, nums))
        temp = s.split('0')
        
        length_temp = len(temp)
        
        maximum = 0
        
        for i in range(length_temp - 1):
            
            length_sub = len(temp[i]) + len(temp[i + 1])
            
            if  length_sub > maximum:
                maximum = length_sub
        
        return maximum
        
        
        
        