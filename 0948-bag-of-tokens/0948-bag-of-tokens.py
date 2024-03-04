class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        result = 0
        score = 0
        q = collections.deque(sorted(tokens))

        while q and (power >= q[0] or score):
            while q and power >= q[0]:
                power -= q.popleft()
                score += 1
            result = max(result, score)
            if q and score:
                power += q.pop()
                score -= 1

        return result