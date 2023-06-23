class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        maximum = 0
        
        for i in range(k):
            maximum += nums[i]
            
        temp = maximum
        
        for i in range(len(nums) - k):
            maximum -= nums[i]
            maximum += nums[i + k]
            
            if maximum >= temp:
                temp = maximum
        
        return temp / k
        