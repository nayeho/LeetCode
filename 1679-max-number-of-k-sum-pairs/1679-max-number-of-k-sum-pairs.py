class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        cnt = Counter(nums)
        
        result = 0
        
        for num in cnt:
            temp = k - num
            if num == temp:
                result += cnt[num] // 2
            elif num < temp:
                result += min(cnt[num], cnt[temp])
        
        return result        