class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        
        return abs(self.countDay(date1) - self.countDay(date2))
        
    def isLeapYear(self, year: int) -> bool:
        
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
    
    def countDay(self, date: str) -> int:
        
        year, month, day = date.split('-')
        year = int(year)
        month = int(month)
        day = int(day)

        days = [31, 29 if self.isLeapYear(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        count = 0

        for i in range(1971, year):
            count += 366 if i % 4 == 0 else 365
        for i in range(month - 1):
            count += days[i]
        count += day
        
        return count
