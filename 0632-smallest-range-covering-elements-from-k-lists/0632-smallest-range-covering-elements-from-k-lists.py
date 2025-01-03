class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        minHeap = [(row[0], i, 0) for i, row in enumerate(nums)]
        heapq.heapify(minHeap)

        maxRange = max(row[0] for row in nums)
        minRange = heapq.nsmallest(1, minHeap)[0][0]
        result = [minRange, maxRange]

        while len(minHeap) == len(nums):
            num, r, c = heapq.heappop(minHeap)
            if c + 1 < len(nums[r]):
                heapq.heappush(minHeap, (nums[r][c + 1], r, c + 1))
                maxRange = max(maxRange, nums[r][c + 1])
                minRange = heapq.nsmallest(1, minHeap)[0][0]
                if maxRange - minRange < result[1] - result[0]:
                    result[0], result[1] = minRange, maxRange

        return result