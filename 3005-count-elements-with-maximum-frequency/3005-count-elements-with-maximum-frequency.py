from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        
        c = Counter(nums).most_common()
        maxFrequency = c[0][1]
        result = 0
        
        for _, cnt in c:
            if cnt == maxFrequency:
                result += cnt
            elif cnt < maxFrequency:
                break
                
        return result
        