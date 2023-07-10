class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        prev_points = 0
        curr_points = 0

        for num in sorted(freq.keys()):
            if num - 1 in freq:
                prev_points, curr_points = curr_points, max(curr_points, prev_points + num * freq[num])
            else:
                prev_points, curr_points = curr_points, curr_points + num * freq[num]

        return max(prev_points, curr_points)