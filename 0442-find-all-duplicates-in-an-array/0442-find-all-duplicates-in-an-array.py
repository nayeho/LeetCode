class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        
        count = [0] * n
        
        for num in nums:
            if count[num - 1] == 0:
                count[num - 1] = 1
            else:
                result.append(num)
                
        return result
        