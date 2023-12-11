class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        element = -1
        count = 0
        
        for a in arr:
            if a != element:
                element = a
                count = 1
            else:
                count += 1
                
            if count > length * 0.25:
                return element
        