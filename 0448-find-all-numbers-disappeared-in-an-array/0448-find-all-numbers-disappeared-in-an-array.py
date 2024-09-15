class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 배열의 값들을 음수로 바꿔서 나타났음을 표현
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])

        # 양수인 숫자들만 반환(나타난 적 없음)
        return [i + 1 for i, num in enumerate(nums) if num > 0]
        
        