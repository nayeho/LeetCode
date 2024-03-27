class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        result = 0
        prod = 1

        j = 0
        for i, num in enumerate(nums):
            prod *= num
            while prod >= k:
                prod /= nums[j]
                j += 1
            result += i - j + 1
  
        return result