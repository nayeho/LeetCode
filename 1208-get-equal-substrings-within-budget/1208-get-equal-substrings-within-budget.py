class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        result = 0
        for i in range(len(s)):
            maxCost -= abs(ord(s[i]) - ord(t[i]))
            if maxCost < 0:
                maxCost += abs(ord(s[result]) - ord(t[result]))
                result += 1

        return len(s) - result