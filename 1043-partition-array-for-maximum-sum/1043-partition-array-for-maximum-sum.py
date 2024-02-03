class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            maximum = -math.inf
            for j in range(1, min(i, k) + 1):
                maximum = max(maximum, arr[i - j])
                dp[i] = max(dp[i], dp[i - j] + maximum * j)

        return dp[n]