class Solution:

    visited = [] # 각 방의 방문 체크 확인을 위한 리스트
    rooms = [[]] # canVisitAllRooms 함수의 입력으로 주어진 rooms 배열을 담아주기 위한 리스트
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        self.visited = [False] * len(rooms)
        self.rooms = rooms
 
        self.dfs(0) # 0번 방부터 dfs 탐색
 
        # 방문하지 못한 방이 있을 경우 false 리턴
        if False in self.visited:
            return False
        
        # 모두 방문했을 경우 true 리턴
        return True
 
    def dfs(self, now):
        if self.visited[now]:
            return
        
        # 현재 방 방문 체크
        self.visited[now] = True
        
        # 현재 방에 있는 열쇠들을 탐색하며 아직 방문하지 않은 방일 경우 dfs 재귀적으로 호출
        for room in self.rooms[now]:
            if self.visited[room]:
                continue
 
            self.dfs(room)
