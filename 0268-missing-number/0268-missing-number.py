class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        n = len(nums)
        full_total = n * (n + 1) // 2
        total = sum(nums)
        
        return full_total - total
        