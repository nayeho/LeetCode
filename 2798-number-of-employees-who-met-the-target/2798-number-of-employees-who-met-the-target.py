class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        
        cnt = 0
        
        for h in hours:
            if h >= target:
                cnt += 1
        
        return cnt
        