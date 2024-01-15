class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        
        maxLiter = 0
        
        while mainTank:
            if mainTank >= 5:
                maxLiter += 5
                mainTank -= 5
                
                if additionalTank > 0:
                    mainTank += 1
                    additionalTank -= 1

            else:
                maxLiter += mainTank
                mainTank = 0
                    
        return maxLiter * 10
        