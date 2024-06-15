from heapq import heappop, heappush

class T:
    def __init__(self, pro, cap):
        self.pro = pro
        self.cap = cap
    
    def __lt__(self, other):
        return self.cap < other.cap

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = []
        maxHeap = []
        for i in range(len(capital)):
            heappush(minHeap, T(profits[i], capital[i]))

        while k > 0:
            while minHeap and minHeap[0].cap <= w:
                project = heappop(minHeap)
                heappush(maxHeap, (-project.pro, project.cap))

            if not maxHeap:
                break

            w -= heappop(maxHeap)[0]
            k -= 1

        return w