class Solution:
    def averageValue(self, nums: List[int]) -> int:
        
        total = 0
        cnt = 0
        
        for n in nums:
            if n % 2 == 0 and n % 3 == 0:
                total += n
                cnt += 1
                
        return 0 if cnt == 0 else total // cnt
        