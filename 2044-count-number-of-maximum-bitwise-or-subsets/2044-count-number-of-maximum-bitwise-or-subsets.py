class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ors = functools.reduce(operator.or_, nums)
        result = 0

        def dfs(i: int, path: int) -> None:
            nonlocal result
            if i == len(nums):
                if path == ors:
                    result += 1
                return

            dfs(i + 1, path)
            dfs(i + 1, path | nums[i])

        dfs(0, 0)
        return result