class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        result = 0
        mx = -math.inf

        for i, a in enumerate(arr):
            mx = max(mx, a)
            if mx == i:
                result += 1

        return result
        
        
        