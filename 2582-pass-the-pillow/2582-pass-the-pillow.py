class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        
        current = 1
        direction = True
        
        for _ in range(time):
            if direction:
                if current < n:
                    current += 1
                else:
                    current -= 1
                    direction = not direction
            else:
                if current > 1:
                    current -= 1
                else:
                    current += 1
                    direction = not direction
                    
        return current
        