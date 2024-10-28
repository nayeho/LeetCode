class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort(reverse=True)

        max_num = max(nums)
        dp = [0] * (max_num + 1)

        for num in nums:
            dp[num] = 1
            squared_num = num * num
            if squared_num <= max_num:
                dp[num] += dp[squared_num]

        result = max(dp)
        return -1 if result < 2 else result
