class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        result = 0
        prefix = 0
        prefixToIndex = {0: -1}

        for i, num in enumerate(nums):
            prefix += 1 if num else -1
            result = max(result, i - prefixToIndex.setdefault(prefix, i))

        return result