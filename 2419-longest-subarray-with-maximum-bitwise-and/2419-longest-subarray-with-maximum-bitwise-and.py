class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        result = 0
        maxIndex = 0
        sameNumLength = 0

        for i, num in enumerate(nums):
            if nums[i] == nums[maxIndex]:
                sameNumLength += 1
                result = max(result, sameNumLength)
            elif nums[i] > nums[maxIndex]:
                maxIndex = i
                sameNumLength = 1
                result = 1
            else:
                sameNumLength = 0

        return result