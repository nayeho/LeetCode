class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        xors = [0] * (len(arr) + 1)

        for i, a in enumerate(arr):
            xors[i + 1] = xors[i] ^ a

        for left, right in queries:
            result.append(xors[left] ^ xors[right + 1])

        return result