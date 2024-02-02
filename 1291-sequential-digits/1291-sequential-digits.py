from queue import Queue
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        q = collections.deque([num for num in range(1, 10)])

        while q:
            num = q.popleft()
            if num > high:
                return result
            if low <= num and num <= high:
                result.append(num)
            lastDigit = num % 10
            if lastDigit < 9:
                q.append(num * 10 + lastDigit + 1)

        return result