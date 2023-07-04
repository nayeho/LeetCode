class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        result = c.most_common()[-1][0]
        # print(c.most_common()[-1][0])
        
        
        return result
        