class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        i = 0
        j = int(sqrt(c))

        while i <= j:
            check = i * i + j * j
            if check == c:
                return True
            if check < c:
                i += 1
            else:
                j -= 1

        return False