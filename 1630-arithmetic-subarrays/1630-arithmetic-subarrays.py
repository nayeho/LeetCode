class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        
        result = []
        m = len(l)
        
        for i in range(m):
            subArray = nums[l[i] : r[i] + 1]
            result.append(self.checkArithmetic(subArray))
        
        return result
        
    def checkArithmetic(self, nums: List[int]) -> bool:
        # a1 = a
        # a2 = a + d
        # a3 = a + 2d
        # a4 = a + 3d
        
        # Sn = n * (a1 + a1 + (n - 1)d) / 2
        # Sn = n * (a1 + an) / 2
        
        # 4, 6, 5
        
        a1 = min(nums)
        an = max(nums)
        n = len(nums)
        
        Sn = n * (a1 + an) // 2
        
        # 2Sn / n = 2a1 + (n - 1)d
        # d = (2Sn / n - 2a1) / (n - 1)
        d = (2 * Sn / n - 2 * a1) / (n - 1)
        
        if int(d) != d:
            return False
        
        d = int(d)
        
        nums.sort()
        
        for i in range(1, n):
            if nums[i] == a1 + (i) * d:
                pass
            else:
                return False
        
        return True
        