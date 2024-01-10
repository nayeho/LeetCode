class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        result = [0] * num_people
        
        check = 0
        
        while 1:
            order = check % num_people
            
            distribute = check + 1
            if candies >= distribute:
                result[order] += distribute
                candies -= distribute
            else:
                result[order] += candies
                break
                
            check += 1
        
        return result
    
