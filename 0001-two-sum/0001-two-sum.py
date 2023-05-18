class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # try dictionary
        temp = {}
        
        for i in range(len(nums)):
            if nums[i] in temp:
                return [temp[nums[i]], i]
            
            temp[target - nums[i]] = i
        
        