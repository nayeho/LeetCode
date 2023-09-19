class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        s = set()
        for num in nums:
            before = len(s)
            s.add(num)
            after = len(s)
            
            if before == after:
                return num
            
        return -1
        
            
        