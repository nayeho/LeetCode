class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxCandy = max(candies)
        
        result = []
        
        for candy in candies:
            if candy + extraCandies >= maxCandy:
                result.append(True)
            else:
                result.append(False)
        
        return result
        
        