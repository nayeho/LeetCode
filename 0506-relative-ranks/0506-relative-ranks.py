class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        result = [None] * n
        indices = list(range(n))

        indices.sort(key=lambda x: score[x], reverse=True)

        for i in range(n):
            if i == 0:
                result[indices[0]] = "Gold Medal"
            elif i == 1:
                result[indices[1]] = "Silver Medal"
            elif i == 2:
                result[indices[2]] = "Bronze Medal"
            else:
                result[indices[i]] = str(i + 1)

        return result