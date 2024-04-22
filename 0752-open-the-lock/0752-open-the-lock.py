class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)
        if '0000' in seen:
            return -1
        if target == '0000':
            return 0

        result = 0
        q = collections.deque(['0000'])

        while q:
            result += 1
            for _ in range(len(q)):
                word = q.popleft()
                for i in range(4):
                    cache = word[i]
                    word = word[:i] + str((int(word[i]) + 1) % 10) + word[i+1:]
                    if word == target:
                        return result
                    if word not in seen:
                        q.append(word)
                        seen.add(word)
                    word = word[:i] + cache + word[i+1:]
                    word = word[:i] + str((int(word[i]) - 1) % 10) + word[i+1:]
                    if word == target:
                        return result
                    if word not in seen:
                        q.append(word)
                        seen.add(word)
                    word = word[:i] + cache + word[i+1:]

        return -1