class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        map1 = [[] for _ in range(n)]
        visit = [False for _ in range(n)]

        for connection in connections:
            a = connection[0]
            b = connection[1]

            map1[a].append(b)
            map1[b].append(-a)


        def dfs(node: int):
            visit[node] = True
            answer = 0

            for n in map1[node]:
                if visit[abs(n)] == False:
                    if n >= 0:
                        answer += 1
                    answer += dfs(abs(n))
            
            return answer

        return dfs(0)