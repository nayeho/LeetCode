class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        result = [[0] * n for _ in range(m)]

        for i, num in enumerate(original):
            result[i // n][i % n] = num

        return result
        