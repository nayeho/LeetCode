class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def dfs(start: int, seen: set) -> int:
            if start == len(s):
                return len(seen)
            
            max_splits = 0
            for i in range(start, len(s)):
                substring = s[start:i + 1]
                if substring not in seen:
                    seen.add(substring)
                    max_splits = max(max_splits, dfs(i + 1, seen))
                    seen.remove(substring)
            return max_splits
        
        return dfs(0, set())
