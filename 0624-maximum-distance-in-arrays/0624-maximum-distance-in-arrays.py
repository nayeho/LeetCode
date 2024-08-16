class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        result = 0
        mn = 10000
        mx = -10000

        for A in arrays:
            result = max(result, A[-1] - mn, mx - A[0])
            mn = min(mn, A[0])
            mx = max(mx, A[-1])

        return result