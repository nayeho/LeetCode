class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dollar_5 = 0
        dollar_10 = 0
        
        for bill in bills:
            if bill == 5:
                dollar_5 += 1
            elif bill == 10:
                if dollar_5 > 0:
                    dollar_5 -= 1
                    dollar_10 += 1
                else:
                    return False
            elif bill == 20:
                if dollar_5 > 0 and dollar_10 > 0:
                    dollar_5 -= 1
                    dollar_10 -= 1
                elif dollar_5 > 2:
                    dollar_5 -= 3
                else:
                    return False
        return True
        