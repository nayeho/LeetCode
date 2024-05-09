class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        result = 0
        check = 0

        happiness.sort(reverse=True)

        for i in range(k):
            result += max(0, happiness[i] - check)
            check += 1

        return result