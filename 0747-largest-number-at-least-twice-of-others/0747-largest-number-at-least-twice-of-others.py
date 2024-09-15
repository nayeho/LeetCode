class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        c = collections.Counter(nums).most_common()
        c.sort(key = lambda x:x[0])
        
        largest_nums = c[-1][0]
        largest_next_nums = c[-2][0]
        
        return nums.index(largest_nums) if largest_nums >= largest_next_nums * 2 else -1
        