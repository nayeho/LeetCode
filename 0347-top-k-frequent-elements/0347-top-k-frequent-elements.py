class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        s = set(nums)
        
        element = []
        count = []
        result = []
        
        for num in s:
            cnt = nums.count(num)
            element.append(num)
            count.append(cnt)
            
        print(element)
        print(count)
        
        for i in range(k):
        
            idx = count.index(max(count))
            result.append(element[idx])
            
            element.remove(element[idx])
            count.remove(count[idx])
        
        return result
        
        