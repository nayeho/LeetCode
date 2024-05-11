class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        result = math.inf
        qualitySum = 0
        workers = sorted((w / q, q) for q, w in zip(quality, wage))
        maxHeap = []

        for wagePerQuality, q in workers:
            heapq.heappush(maxHeap, -q)
            qualitySum += q
            if len(maxHeap) > k:
                qualitySum += heapq.heappop(maxHeap)
            if len(maxHeap) == k:
                result = min(result, qualitySum * wagePerQuality)

        return result