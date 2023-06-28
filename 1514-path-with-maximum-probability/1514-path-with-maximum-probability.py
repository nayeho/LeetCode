class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        maps = defaultdict(list)
        for i in range(len(edges)):
            maps[edges[i][0]].append((edges[i][1], succProb[i]))
            maps[edges[i][1]].append((edges[i][0], succProb[i]))
        q = [(-1, start)]
        dist = defaultdict(float)
        dist[start] = -1
        while q:
            curdist, cur = heapq.heappop(q)
            if cur == end:
                return -curdist
            for node, prob in maps[cur]:
                tmp = curdist * prob
                if tmp < dist[node]:
                    dist[node] = tmp
                    heapq.heappush(q, (tmp, node))
        return 0
        
        
        
        