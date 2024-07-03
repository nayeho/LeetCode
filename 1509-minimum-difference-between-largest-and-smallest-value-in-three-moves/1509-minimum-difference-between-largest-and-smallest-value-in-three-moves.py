class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0

        result = math.inf

        nums.sort()

        for i in range(4):
            result = min(result, nums[n - 4 + i] - nums[i])

        return result