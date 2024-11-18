class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        if k == 0:
            return result

        summ = 0
        start = 1 if k > 0 else n + k
        end = k if k > 0 else n - 1

        for i in range(start, end + 1):
            summ += code[i]

        for i in range(n):
            result[i] = summ
            summ -= code[start % n]
            start += 1
            end += 1
            summ += code[end % n]

        return result