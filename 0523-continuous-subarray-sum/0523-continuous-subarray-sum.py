class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        check = 0
        idx = {0: -1}

        for i, num in enumerate(nums):
            check += num
            if k != 0:
                check %= k
            if check in idx:
                if i - idx[check] > 1:
                    return True
            else:
                idx[check] = i

        return False