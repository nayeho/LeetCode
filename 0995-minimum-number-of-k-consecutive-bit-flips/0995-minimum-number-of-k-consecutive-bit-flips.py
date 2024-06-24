class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        result = 0
        check = 0

        for i, num in enumerate(nums):
            if i >= k and nums[i - k] == 2:
                check -= 1
            if check % 2 == num:
                if i + k > len(nums):
                    return -1
                result += 1
                check += 1
                nums[i] = 2

        return result