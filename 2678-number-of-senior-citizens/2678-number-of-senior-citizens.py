class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result = 0
        for detail in details:
            age = int(detail[-4:-2])
            if age > 60:
                result += 1
        
        return result
            
        