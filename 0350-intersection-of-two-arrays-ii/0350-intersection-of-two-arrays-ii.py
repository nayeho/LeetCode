class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        # Two Pointers
        
        nums1.sort()
        nums2.sort()
        
        result = []
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        
        while i < len1 and j < len2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                i += 1
                j += 1
        
        return result
        
        
        