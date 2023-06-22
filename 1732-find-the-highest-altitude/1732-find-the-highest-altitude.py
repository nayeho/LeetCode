class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        if len(gain) == 1:
            return max(gain[0], 0)
        
        highest = gain[0]
        current = gain[0]
        for i in range(1, len(gain)):
            current += gain[i]
            highest = max(current, highest)
            
        return max(highest, 0)
        