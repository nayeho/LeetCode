class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        dic_digit = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        length = len(digits)
        result = []
        
        if length == 0:
            return result
        
        elif length == 1:
            return list(dic_digit[digits])
        
        elif length == 2:
            
            digit_1 = dic_digit[digits[0]]
            digit_2 = dic_digit[digits[1]]
            
            for i in range(len(digit_1)):
                for j in range(len(digit_2)):
                    result.append(digit_1[i] + digit_2[j])
            return result
    
        elif length == 3:
            
            digit_1 = dic_digit[digits[0]]
            digit_2 = dic_digit[digits[1]]
            digit_3 = dic_digit[digits[2]]
            
            for i in range(len(digit_1)):
                for j in range(len(digit_2)):
                    for k in range(len(digit_3)):
                        result.append(digit_1[i] + digit_2[j] + digit_3[k])
            return result
    
        elif length == 4:
            
            digit_1 = dic_digit[digits[0]]
            digit_2 = dic_digit[digits[1]]
            digit_3 = dic_digit[digits[2]]
            digit_4 = dic_digit[digits[3]]
            
            for i in range(len(digit_1)):
                for j in range(len(digit_2)):
                    for k in range(len(digit_3)):
                        for l in range(len(digit_4)):
                            result.append(digit_1[i] + digit_2[j] + digit_3[k] + digit_4[l])
            return result
        
    
    
    
    
                    
        