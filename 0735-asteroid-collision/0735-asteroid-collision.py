class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        result = []
        for star in asteroids:
            while result and star < 0 < result[-1]:
                if result[-1] < -star:
                    result.pop()
                    continue
                elif result[-1] == -star:
                    result.pop()
                break
            else:
                result.append(star)
        return result