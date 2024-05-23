class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        count = collections.Counter(nums)
        dict1 = collections.defaultdict(set)

        for num in nums:
            dict1[num % k].add(num)

        pre = -k
        skip = 0
        pick = 0

        for subset in dict1.values():
            for num in sorted(subset):
                nonEmptyCount = 2**count[num] - 1
                skip, pick = skip + pick, nonEmptyCount * (1 + skip + (0 if num - pre == k else pick))
                pre = num

        return skip + pick