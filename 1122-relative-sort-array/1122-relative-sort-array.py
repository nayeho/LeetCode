class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []
        count = [0] * 1001

        for a in arr1:
            count[a] += 1

        for a in arr2:
            while count[a] > 0:
                result.append(a)
                count[a] -= 1

        for num in range(1001):
            for _ in range(count[num]):
                result.append(num)

        return result