class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        
        # Olog(n) -> Binary
        
        length = len(nums)
        
        if length == 0:
            return [-1, -1]
        elif length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
        elif length == 2:
            if nums[0] == target:
                if nums[1] == target:
                    return [0, 1]
                else:
                    return [0, 0]
            else:
                if nums[1] == target:
                    return [1, 1]
                else:
                    return [-1, -1]
                
        else:
            search = -1
            low = 0
            high = length - 1
            
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    search = mid
                    break
                elif nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
                    
            if search == -1:
                return [-1, -1]
            
            result = [search, search]
            start = search
            end = search
            
            # start
            while start != 0:
                if nums[start] == nums[start - 1]:
                    start -= 1
                else:
                    break
            
            while end != length - 1:
                if nums[end] == nums[end + 1]:
                    end += 1
                else:
                    break
                    
        return [start, end]
                        
                        
                        
                        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            
            
        