class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        result = 0
        i = 0
        check = 1

        while check <= n:
            if i < len(nums) and nums[i] <= check:
                check += nums[i]
                i += 1
            else:
                check += check
                result += 1

        return result