class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        length = len(nums)
        
        k = k % length
        
        for i in range(k):
            temp = nums[-1]
            
            nums.pop()
            nums.insert(0, temp)
            # print(nums)
        