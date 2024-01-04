class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        s1 = list(set(nums1))
        s2 = list(set(nums2))
        
        result = []
        
        len1 = len(s1)
        len2 = len(s2)
        
        if len1 < len2:
            for i in range(len1):
                if s1[i] in s2:
                    result.append(s1[i])
        else:
            for i in range(len2):
                if s2[i] in s1:
                    result.append(s2[i])
        
        return result
        