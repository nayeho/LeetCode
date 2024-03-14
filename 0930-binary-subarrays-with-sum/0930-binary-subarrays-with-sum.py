class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        result = 0
        prefix = 0
        count = collections.Counter({0: 1})

        for num in nums:
            prefix += num
            result += count[prefix - goal]
            count[prefix] += 1

        return result