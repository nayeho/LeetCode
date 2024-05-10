class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        result = [0, 1]
        l = 0
        r = 1

        while True:
            m = (l + r) / 2
            result[0] = 0
            count = 0
            j = 1

            for i in range(n):
                while j < n and arr[i] > m * arr[j]:
                    j += 1
                count += n - j
                if j == n:
                    break
                if result[0] * arr[j] < result[1] * arr[i]:
                    result[0] = arr[i]
                    result[1] = arr[j]

            if count < k:
                l = m
            elif count > k:
                r = m
            else:
                return result