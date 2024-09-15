class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count_U = moves.count('U')
        count_D = moves.count('D')
        count_L = moves.count('L')
        count_R = moves.count('R')
        
        # print(count_U, count_D, count_L, count_R)
        if (count_U == count_D) and (count_L == count_R):
            return True
        
        return False