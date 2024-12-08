class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        result = 0
        maxValue = 0
        evts = []

        for s, e, v in events:
            evts.append((s, 1, v))
            evts.append((e + 1, 0, v))

        evts.sort()

        for _, isStart, value in evts:
            if isStart:
                result = max(result, value + maxValue)
            else:
                maxValue = max(maxValue, value)

        return result