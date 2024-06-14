class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        result = 0
        check = 0

        for num in sorted(nums):
            result += max(check - num, 0)
            check = max(check, num) + 1

        return result