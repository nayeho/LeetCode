class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        
        for num in range(low, high + 1):
            if 10 <= num <= 99:
                first = num // 10
                last = num % 10
                
                if first == last:
                    result += 1
                
            elif 1000 <= num <= 9999:
                first = num // 100
                last = num % 100
                
                first_sum = first // 10 + first % 10
                last_sum = last // 10 + last % 10
                
                if first_sum == last_sum:
                    result += 1
                    print(num)
        
        return result
        
        
        