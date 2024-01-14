class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        
        length = len(nums)
        
        temp = []
        
        for i in range(length):
            temp.append(nums[i][i])
            temp.append(nums[i][length - 1 - i])
            
        temp.sort(reverse=True)
        
        for i in range(len(temp)):
            if self.isPrime(temp[i]):
                return temp[i]
            
        return 0
        
    def isPrime(self, num) -> bool:
        
        if num == 1:
            return False
        
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

        return True
        