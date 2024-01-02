import copy
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        copy_list = copy.deepcopy(nums)
        
        while nums != []:
            temp = []
            for i in range(len(nums)):
                if nums[i] not in temp:
                    temp.append(nums[i])
                    copy_list.remove(nums[i])

            result.append(temp)

            nums = copy.deepcopy(copy_list)

            # print('nums', nums)
            # print('temp', temp)
        
        return result
        
        