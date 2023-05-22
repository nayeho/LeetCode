class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        dict_two = {}
        for i, num in enumerate(numbers):
            different = target - num
            if different in dict_two:
                return [dict_two[different] + 1, i + 1]
            else:
                dict_two[num] = i    
        