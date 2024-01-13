from collections import Counter
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        
        c1 = Counter(s)
        c2 = Counter(t)
        c2_sub = c1.subtract(c2)
        
        return sum(abs(value) for value in c1.values()) // 2
        