class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = 0
        check = 0
        count = [0] * k
        count[0] = 1

        for num in nums:
            check = (check + num % k + k) % k
            result += count[check]
            count[check] += 1

        return result