class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0:
            return '0'

        result = ''

        if (numerator < 0) ^ (denominator < 0):
            result += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)
        result += str(numerator // denominator)

        if numerator % denominator == 0:
            return result

        result += '.'
        dict = {}

        remainder = numerator % denominator
        while remainder:
            if remainder in dict:
                result = result[:dict[remainder]] + '(' + result[dict[remainder]:] + ')'
                break
            dict[remainder] = len(result)
            remainder *= 10
            result += str(remainder // denominator)
            remainder %= denominator

        return result
        