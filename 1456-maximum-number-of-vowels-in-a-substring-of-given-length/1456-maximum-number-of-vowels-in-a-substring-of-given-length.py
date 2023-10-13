class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        answer = 0
        maximum = 0
        kVowels = 'aeiou'

        for i, c in enumerate(s):
            
            if c in kVowels:
                maximum += 1
                
            if i >= k and s[i - k] in kVowels:
                maximum -= 1
            
            answer = max(answer, maximum)

        return answer
        
        
        
        
#         Time Limit Exceeded        
#         length = len(s)
#         loop = length - k + 1
        
#         counts = []
        
#         for i in range(loop):
            
#             temp = s[i : i + k]
            
#             count = 0
#             for word in temp:
#                 if word in ['a', 'e', 'i', 'o', 'u']:
#                     count += 1
                
#             counts.append(count)
            
#         return max(counts)
        