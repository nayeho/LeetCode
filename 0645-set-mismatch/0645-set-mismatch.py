from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        c = Counter(nums).most_common()
        repeat = int(c[0][0])
        
        n = len(nums)
        S = n * (n + 1) // 2
        
        loss = S - (sum(nums) - repeat)
        
        return [repeat, loss]