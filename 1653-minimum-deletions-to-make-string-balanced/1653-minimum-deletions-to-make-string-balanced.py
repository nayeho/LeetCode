class Solution:
    def minimumDeletions(self, s: str) -> int:
        result = 0
        check = 0

        for c in s:
            if c == 'a':
                result = min(result + 1, check)
            else:
                check += 1

        return result