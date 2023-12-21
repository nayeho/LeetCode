from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks).most_common()
        
        if cnt[-1][1] < 2:
            return -1
        
        result = 0
        
        for _, ea in cnt:
            if ea % 3 == 0:
                result += ea // 3
            else:
                result += ea // 3 + 1
                
        return result    