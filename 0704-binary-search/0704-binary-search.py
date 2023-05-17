class Solution:
    def search(self, nums: List[int], target: int) -> int:


        lowIndex = 0
        highIndex = len(nums) - 1
        

        while highIndex >= lowIndex:
            middleIndex = (lowIndex + highIndex) // 2
            if nums[middleIndex] == target:
                return middleIndex
            elif nums[middleIndex] > target:
                highIndex = middleIndex - 1
            else:
                lowIndex = middleIndex + 1

        return -1
        

        
        