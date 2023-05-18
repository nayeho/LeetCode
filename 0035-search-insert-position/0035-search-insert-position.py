class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        length = len(nums)
        
        if target > nums[-1]:
            return length
        
        for i in range(length):
            if target <= nums[i]:
                return i
        
        