from collections import Counter
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        
        c = Counter(deck)
        return functools.reduce(math.gcd, c.values()) >= 2