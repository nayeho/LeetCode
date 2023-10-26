class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        N = len(arr)
        arr.sort()
        modulo = 10**9 + 7
        dp = [1]*N
        
        idxs = {}                       # arr안의 숫자에 대한 index를 저장
        for idx, num in enumerate(arr):
            idxs[num] = idx
        
        for i in range(1, N):
            for j in range(i):
                if arr[i]%arr[j] == 0:  # arr[i]가 arr[j]의 배수라면
                    if arr[i]//arr[j] in idxs:  # arr[j] * x = arr[i]를 만족시키는 x가 arr에 존재한다면
                        dp[i] += dp[idxs[arr[i]//arr[j]]] * dp[j]   # 그 x의 index를 idx라 할 때, dp[i] += dp[idx]*dp[j]
                        dp[i] %= modulo
                        
        return sum(dp)%modulo
        