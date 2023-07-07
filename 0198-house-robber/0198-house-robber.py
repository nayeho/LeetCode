class Solution:
    def rob(self, nums: List[int]) -> int:
        former, later = 0, 0
        for i in nums:
            former, later = later, max(former + i, later)
        return later
        