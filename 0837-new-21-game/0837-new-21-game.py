class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        
        
        if k == 0:
            return 1.0
        
        windowSum = 0
        for i in range(k, k + maxPts):
            windowSum += 1 if i <= n else 0
            
        dp = {} # start at score -> probability
        for i in range(k - 1, -1, -1):
            dp[i] = windowSum / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = dp.get(i + maxPts, 1)
            windowSum += dp[i] - remove
            
        return dp[0]
        
        
        
        
        
        
#         cache = {}
        
#         # Start at score, return probability
        
#         def dfs(score):
#             if score >= k:
#                 return 1 if score <= n else 0
#             if score in cache:
#                 return cache[score]
            
#             prob = 0
#             for i in range(1, maxPts + 1):
#                 prob += dfs(score + i)
                
#             cache[score] = prob / maxPts
#             return cache[score]
    
#         return dfs(0)
        