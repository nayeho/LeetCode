class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        result = 0
        summ = 0
        bannedSet = set(banned)

        for i in range(1, n + 1):
            if i not in bannedSet and summ + i <= maxSum:
                result += 1
                summ += i

        return result