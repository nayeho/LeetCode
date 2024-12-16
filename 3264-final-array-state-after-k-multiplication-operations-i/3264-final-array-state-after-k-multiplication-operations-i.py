class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        result = [0] * len(nums)
        minHeap = [(num, i) for i, num in enumerate(nums)]
        heapq.heapify(minHeap)

        for _ in range(k):
            num, i = heapq.heappop(minHeap)
            heapq.heappush(minHeap, (num * multiplier, i))

        for num, i in minHeap:
            result[i] = num

        return result