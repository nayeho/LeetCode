class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1

        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        result = 0
        dvd = abs(dividend)
        dvs = abs(divisor)

        while dvd >= dvs:
            k = 1
            while k * 2 * dvs <= dvd:
                k <<= 1
            dvd -= k * dvs
            result += k

        return sign * result
        
#         if dividend == 0:
#             return 0
        
#         if divisor == 1:
#             return dividend
        
#         if dividend == -2**31 and divisor == -1:
#             return 2**31 - 1
        
#         if divisor == -1:
#             return -dividend
            
#         result = 0
            
#         if dividend > 0:
#             if divisor > 0:
#                 # 10, 3 // 10 - 3 - 3 - 3
#                 while 1:
#                     dividend -= divisor
#                     if dividend < 0:
#                         return result
#                     else:
#                         result += 1
#             else:
#                 # 10, -3 // 10 -3 -3 -3
#                 while 1:
#                     dividend += divisor
#                     if dividend < 0:
#                         return result
#                     else:
#                         result -= 1
#         else:
#             if divisor > 0:
#                 # -10, 3 // -10 +3 +3 +3
#                 while 1:
#                     dividend += divisor
#                     if dividend > 0:
#                         return result
#                     else:
#                         result -= 1
#             else:
#                 # -10, -3 // -10 +3 +3 +3
#                 while 1:
#                     dividend -= divisor
#                     if dividend > 0:
#                         return result
#                     else:
#                         result += 1
#         return -1
        
        
        