class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
        result = []
        
        n = len(nums) / 3
        
        dict_num = {}
        
        for num in nums:
            
            s = str(num)
            
            if s in dict_num:
                dict_num[s] += 1
            else:
                dict_num[s] = 1
        
        # print(dict_num)
        
        
        for key, value in dict_num.items():
            if value > n:
                result.append(int(key))
                
        return result
        
        