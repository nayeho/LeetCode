from collections import Counter
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        c = Counter(s).most_common()
        above_two = []
        length = len(s)
        result = -1
        
        for i, cnt in c:
            if cnt > 1:
                above_two.append(i)
        
        print(c)
        print(above_two)
        print(s)
        print(s[::-1])
        reverse_s = s[::-1]
        
        for element in above_two:
            first = s.index(element)
            last = reverse_s.index(element)
            
            distance = length - 1 - last - first - 1
            
            if distance > result:
                result = distance
        
        return result