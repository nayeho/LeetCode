class Solution:
    def countPoints(self, rings: str) -> int:
        
        colors = ['R', 'G', 'B']
        numbers = [str(x) for x in range(10)]
        result = 0
        
        for number in numbers:
            color_r = colors[0] + number
            color_g = colors[1] + number
            color_b = colors[2] + number
            
            count_r = rings.count(color_r)
            count_g = rings.count(color_g)
            count_b = rings.count(color_b)
            
            if count_r >= 1 and count_g >= 1 and count_b >= 1:
                result += 1
                
        return result
                
        