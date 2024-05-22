class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def isPalindrome(s: str) -> bool:
            return s == s[::-1]

        def dfs(s: str, j: int, path: List[str], result: List[List[str]]) -> None:
            if j == len(s):
                result.append(path)
                return

            for i in range(j, len(s)):
                if isPalindrome(s[j: i + 1]):
                    dfs(s, i + 1, path + [s[j: i + 1]], result)

        dfs(s, 0, [], result)
        return result