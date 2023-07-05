class Solution:
    def intToRoman(self, num: int) -> str:
        
        result = ''
        
        digits_1000 = str(num // 1000)
        digits_100 = str(num % 1000 // 100)
        digits_10 = str(num % 100 // 10)
        digits_1 = str(num % 10)
        
        dict_1000 = {'3':'MMM', '2':'MM', '1':'M', '0':''}
        dict_100 = {'9':'CM','8':'DCCC', '7':'DCC', '6':'DC', '5':'D', '4':'CD', '3':'CCC', '2':'CC', '1':'C', '0':''}
        dict_10 = {'9':'XC','8':'LXXX', '7':'LXX', '6':'LX', '5':'L', '4':'XL', '3':'XXX', '2':'XX', '1':'X', '0':''}
        dict_1 = {'9':'IX','8':'VIII', '7':'VII', '6':'VI', '5':'V', '4':'IV', '3':'III', '2':'II', '1':'I', '0':''}
        
        result += dict_1000[digits_1000]
        result += dict_100[digits_100]
        result += dict_10[digits_10]
        result += dict_1[digits_1]

        return result
        