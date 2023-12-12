class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        bigNumberFirst = 0
        bigNumberSecond = 0
        
        length = len(nums)
        
        if length == 2:
            return (nums[0] - 1) * (nums[1] - 1)
        
        if nums[0] > nums[1]:
            bigNumberFirst = nums[0]
            bigNumberSecond = nums[1]
        else:
            bigNumberFirst = nums[1]
            bigNumberSecond = nums[0]
        
        for i in range(2, length):
            if nums[i] > bigNumberSecond:
                if nums[i] > bigNumberFirst:
                    bigNumberSecond = bigNumberFirst
                    bigNumberFirst = nums[i]
                    
                else:
                    bigNumberSecond = nums[i]
            
                    
        return (bigNumberFirst - 1) * (bigNumberSecond - 1)
        