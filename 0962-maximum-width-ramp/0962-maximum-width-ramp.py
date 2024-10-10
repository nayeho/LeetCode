class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        result = 0
        stack = []

        for i, num in enumerate(nums):
            if stack == [] or num <= nums[stack[-1]]:
                stack.append(i)

        for i, num in reversed(list(enumerate(nums))):
            while stack and num >= nums[stack[-1]]:
                result = max(result, i - stack.pop())

        return result