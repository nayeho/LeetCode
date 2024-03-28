class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        count = collections.Counter()
        result = 0

        l = 0
        for r, num in enumerate(nums):
            count[num] += 1
            while count[num] == k + 1:
                count[nums[l]] -= 1
                l += 1
            result = max(result, r - l + 1)

        return result  