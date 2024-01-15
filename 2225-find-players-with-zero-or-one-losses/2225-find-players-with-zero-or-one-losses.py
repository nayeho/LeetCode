class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        answer = [[] for _ in range(2)]
        
        lossesCount = collections.Counter()

        for winner, loser in matches:
            if winner not in lossesCount:
                lossesCount[winner] = 0
            lossesCount[loser] += 1

        for player, nLosses in lossesCount.items():
            if nLosses < 2:
                answer[nLosses].append(player)

        return [sorted(answer[0]), sorted(answer[1])]
        