class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        temp = [[] for _ in range(len(s) + 1)]

        for c, freq in collections.Counter(s).items():
            temp[freq].append(c)

        for freq in reversed(range(len(temp))):
            for c in temp[freq]:
                result.append(c * freq)

        return ''.join(result)