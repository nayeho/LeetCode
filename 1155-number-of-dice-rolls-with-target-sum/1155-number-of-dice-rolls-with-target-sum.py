class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [1] + [0] * target

        for _ in range(n):
            newDp = [0] * (target + 1)
            for i in range(1, k + 1):
                for t in range(i, target + 1):
                    newDp[t] += dp[t - i]
                    newDp[t] %= MOD
            dp = newDp

        return dp[target]