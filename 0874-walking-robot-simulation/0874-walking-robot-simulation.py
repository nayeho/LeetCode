class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        d = 0
        obstaclesSet = {(ox, oy) for ox, oy in obstacles}
        result = 0

        for c in commands:
            if c == -1:
                d = (d + 1) % 4
            elif c == -2:
                d = (d + 3) % 4
            else:
                for _ in range(c):
                    nx, ny = x + dirs[d][0], y + dirs[d][1]
                    if (nx, ny) in obstaclesSet:
                        break
                    x, y = nx, ny
                result = max(result, x * x + y * y)

        return result