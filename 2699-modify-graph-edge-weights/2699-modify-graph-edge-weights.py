#review
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        kMax = 2_000_000_000
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            if w == -1:
                continue
            graph[u].append((v, w))
            graph[v].append((u, w))

        distToDestination = self._dijkstra(graph, source, destination)
        if distToDestination < target:
            return []
        if distToDestination == target:
            for edge in edges:
                if edge[2] == -1:
                    edge[2] = kMax
            return edges

        for i, (u, v, w) in enumerate(edges):
            if w != -1:
                continue
            edges[i][2] = 1
            graph[u].append((v, 1))
            graph[v].append((u, 1))
            distToDestination = self._dijkstra(graph, source, destination)
            if distToDestination <= target:
                edges[i][2] += target - distToDestination
                for j in range(i + 1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = kMax
                return edges

        return []

    def _dijkstra(self, graph: list[list[int]], src: int, dst: int) -> int:
        dist = [math.inf] * len(graph)
        minHeap = []
        dist[src] = 0
        heapq.heappush(minHeap, (dist[src], src))

        while minHeap:
            d, u = heapq.heappop(minHeap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    heapq.heappush(minHeap, (dist[v], v))

        return dist[dst]