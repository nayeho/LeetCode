class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        dp = [collections.defaultdict(int) for i in range(len(nums))]
        
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    result += dp[j][diff]
        return result