class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        isOdd = True if nums[0] % 2 == 1 else False
        
        for i in range(1, n):
            if nums[i] % 2 == 0:
                if not isOdd:
                    return False
                else:
                    isOdd = False
            else:
                if isOdd:
                    return False
                else:
                    isOdd = True
        return True
            