class Solution:
    def totalMoney(self, n: int) -> int:

        week = n // 7
        
        if n % 7 == 0:
            return 28 * week + 7 * ((week - 1) * (week)) // 2
        else:
            pre = self.totalMoney(week * 7)
            days = n % 7
            result = pre + week * days + ((days + 1) * (days)) // 2
            return result            
        