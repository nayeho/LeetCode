class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        temp = []
        set_arr = set(arr)
        for i in set_arr:
            temp.append(arr.count(i))
            
        len_before = len(temp)
        len_after = len(list(set(temp)))
        
        return len_before == len_after