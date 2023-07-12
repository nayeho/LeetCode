class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        
        dt = defaultdict(list)
        status = defaultdict(int) # if visiting this node change status to 1 else 0
        res = []
        
        for i, val in enumerate(graph):
            dt[i] = val
            
        def dfs(num):
            if dt[num] == []: return True
            
            if status[num] == 1: return False
            
            status[num] = 1
            
            for val in dt[num]:
                if not dfs(val):
                    return False
                
            dt[num] = []
            status[num] = 0
            
            return True
            
        for num in range(len(graph)):
            if dfs(num):
                res.append(num)

        return res
        