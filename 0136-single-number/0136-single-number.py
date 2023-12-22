class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        length = len(nums)
        temp = []
        
        if length == 1:
            return nums[0]
        
        for num in nums:
            if num not in temp:
                temp.append(num)
            else:
                temp.remove(num)
                
        return temp[0]
        