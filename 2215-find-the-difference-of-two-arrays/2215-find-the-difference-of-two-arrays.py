class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        temp1 = nums1
        temp2 = nums2
        
        temp1 = [i for i in nums1 if i not in nums2]
        temp2 = [i for i in nums2 if i not in nums1]
        
        result = [list(set(temp1)), list(set(temp2))]
        return result