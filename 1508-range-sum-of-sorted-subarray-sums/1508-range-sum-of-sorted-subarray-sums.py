class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1_000_000_007

        def subarraysAndSumNoGreaterThan(m: int) -> tuple:
            count = 0
            total = 0
            sum_ = 0
            window = 0

            i = 0
            for j in range(n):
                sum_ += nums[j] * (j - i + 1)
                window += nums[j]
                while window > m:
                    sum_ -= window
                    window -= nums[i]
                    i += 1
                count += j - i + 1
                total += sum_

            return count, total

        L = min(nums)
        R = sum(nums)

        def firstKSubarraysSum(k: int) -> int:
            l = L
            r = R

            while l < r:
                m = l + (r - l) // 2
                if subarraysAndSumNoGreaterThan(m)[0] < k:
                    l = m + 1
                else:
                    r = m

            count, total = subarraysAndSumNoGreaterThan(l)
            return total - l * (count - k)

        return (firstKSubarraysSum(right) - firstKSubarraysSum(left - 1)) % MOD
