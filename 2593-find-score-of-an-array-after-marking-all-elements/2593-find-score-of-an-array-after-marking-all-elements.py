class Solution:
    def findScore(self, nums: List[int]) -> int:
        result = 0
        seen = set()

        for num, i in sorted([(num, i) for i, num in enumerate(nums)]):
            if i in seen:
                continue
            seen.add(i - 1)
            seen.add(i + 1)
            seen.add(i)
            result += num

        return result