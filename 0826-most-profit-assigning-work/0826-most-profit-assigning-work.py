class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        result = 0
        check = sorted(zip(difficulty, profit))
        worker.sort(reverse=1)

        i = 0
        maxProfit = 0

        for w in sorted(worker):
            while i < len(check) and w >= check[i][0]:
                maxProfit = max(maxProfit, check[i][1])
                i += 1
            result += maxProfit

        return result