class Solution:
    def dayOfYear(self, date: str) -> int:
        
        year, month, day = date.split('-')
        result = 0
        
        day_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        year = int(year)
        month = int(month)
        day = int(day)
        
        for i in range(month - 1):
            result += day_of_month[i]
            
        result += day
        
        if year % 400 == 0 and month >= 3:
            return result + 1
        
        if year % 100 == 0:
            return result
        
        if year % 4 == 0 and month >= 3:
            result += 1
        
        return result
        
        