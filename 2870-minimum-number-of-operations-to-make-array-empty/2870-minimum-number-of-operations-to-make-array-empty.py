from collections import Counter
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        c = Counter(nums).most_common()
        result = 0
        
        if c[-1][1] < 2:
            return -1
        
        for _, cnt in c:
            if cnt % 3 == 0:
                pass
            else:
                result += 1

            result += cnt // 3
                
        return result
        
        