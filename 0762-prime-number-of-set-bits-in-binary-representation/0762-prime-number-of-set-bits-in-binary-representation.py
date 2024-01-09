class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        
        # 10e6 -> 1000000 -> 11110100001001000000(2)
        # 최대 1의 개수 : 19개
        primes = [2, 3, 5, 7, 11, 13, 17, 19]
        result = 0
        
        for i in range(left, right + 1):
            if bin(i).count('1') in primes:
                result += 1
        
        return result