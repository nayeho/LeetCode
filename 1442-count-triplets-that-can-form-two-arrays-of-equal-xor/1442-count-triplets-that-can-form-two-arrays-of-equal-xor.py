class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        result = 0
        xors = [0]
        prefix = 0

        for i, a in enumerate(arr):
            prefix ^= a
            xors.append(prefix)

        for i in range(1, len(arr)):
            for j in range(0, i):
                xors_j = xors[i] ^ xors[j]
                for k in range(i, len(arr)):
                    xors_k = xors[k + 1] ^ xors[i]
                    if xors_j == xors_k:
                        result += 1

        return result