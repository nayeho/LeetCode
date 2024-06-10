class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != result[i]:
                count += 1
        return count