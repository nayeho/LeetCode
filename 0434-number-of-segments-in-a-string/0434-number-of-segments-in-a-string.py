class Solution:
    def countSegments(self, s: str) -> int:
        s_split = s.split(' ')
        
        cnt = s_split.count('')
        
        return len(s_split) - cnt
        