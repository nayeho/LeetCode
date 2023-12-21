class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        
        cnt = 0
        
        length = len(costs)
        
        for i in range(length):
            if coins >= costs[i]:
                coins -= costs[i]
                cnt += 1
            else:
                break
                
        return cnt
        