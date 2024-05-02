class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        result = -1
        seen = set()

        for num in nums:
            if -num in seen:
                result = max(result, abs(num))
            else:
                seen.add(num)

        return result    