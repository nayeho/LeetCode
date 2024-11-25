class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = 2, 3
        goal = '123450'
        start = ''.join(str(num) for row in board for num in row)

        if start == goal:
            return 0

        queue = collections.deque([start])
        seen = set([start])

        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                s = queue.popleft()
                zero_index = s.index('0')
                i, j = divmod(zero_index, n)
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if x < 0 or x >= m or y < 0 or y >= n:
                        continue
                    swapped_index = x * n + y
                    sb = list(s)
                    sb[zero_index], sb[swapped_index] = sb[swapped_index], sb[zero_index]
                    t = ''.join(sb)
                    if t == goal:
                        return step
                    if t not in seen:
                        queue.append(t)
                        seen.add(t)

        return -1
