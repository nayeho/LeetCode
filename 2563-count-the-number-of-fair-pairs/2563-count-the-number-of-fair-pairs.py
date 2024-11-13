class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def countLess(summ: int) -> int:
            result = 0
            i = 0
            j = len(nums) - 1
            while i < j:
                while i < j and nums[i] + nums[j] > summ:
                    j -= 1
                result += j - i
                i += 1
            return result

        return countLess(upper) - countLess(lower - 1)