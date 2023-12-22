class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        if n > 45 or n < 3:
            return []
        
        result = []

        def dfs(k: int, n: int, s: int, path: List[int]) -> None:
            if k == 0 and n == 0:
                result.append(path)
                return
            if k == 0 or n < 0:
                return

            for i in range(s, 10):
                dfs(k - 1, n - i, i + 1, path + [i])

        dfs(k, n, 1, [])
        return result
        