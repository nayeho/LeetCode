class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        result = 0
        dist = [[math.inf] * 26 for _ in range(26)]

        for a, b, c in zip(original, changed, cost):
            u = ord(a) - ord('a')
            v = ord(b) - ord('a')
            dist[u][v] = min(dist[u][v], c)

        for k in range(26):
            for i in range(26):
                if dist[i][k] < math.inf:
                    for j in range(26):
                        if dist[k][j] < math.inf:
                            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        for s, t in zip(source, target):
            if s == t:
                continue
            u = ord(s) - ord('a')
            v = ord(t) - ord('a')
            if dist[u][v] == math.inf:
                return -1
            result += dist[u][v]

        return result