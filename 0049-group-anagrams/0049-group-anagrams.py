from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        temp = dict()
        result = []
        
        for s in strs:
            c = Counter(s).most_common()
            c.sort()
            c = str(c)
            if c in temp:
                temp[str(c)].append(s)
            else:
                temp[str(c)] = [s]
        
        for item in temp.values():
            result.append(item)
        
        return result
        