class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        # non-leap year
        
        result = 0
        
        day_arriveAlice = self.countDay(arriveAlice)
        day_leaveAlice = self.countDay(leaveAlice)
        day_arriveBob = self.countDay(arriveBob)
        day_leaveBob = self.countDay(leaveBob)
        
        alice = []
        for i in range(day_arriveAlice, day_leaveAlice + 1):
            alice.append(i)
            
        bob = []
        for i in range(day_arriveBob, day_leaveBob + 1):
            bob.append(i)
            
        for d in alice:
            if d in bob:
                result += 1
                
        return result
        
        
    def countDay(self, date: str) -> int:
        count = 0
        
        month, day = date.split('-')
        month = int(month)
        day = int(day)
        
        day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        for i in range(month):
            count += day_of_month[i]
            
        return count + day
        