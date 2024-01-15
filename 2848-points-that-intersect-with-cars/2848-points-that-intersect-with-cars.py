class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        result = []
        
        for start, end in nums:
            for i in range(start, end + 1):
                if i not in result:
                    result.append(i)
            
        return len(result)