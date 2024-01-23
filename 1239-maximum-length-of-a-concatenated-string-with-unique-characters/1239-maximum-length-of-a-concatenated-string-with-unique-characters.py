class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []

        for s in arr:
            mask = self.getMask(s)
            if mask != -1:
                masks.append(mask)

        return self.dfs(masks, 0, 0)

    def dfs(self, masks, s, used):
        res = bin(used).count('1')
        for i in range(s, len(masks)):
            if (used & masks[i]) == 0:
                res = max(res, self.dfs(masks, i + 1, used | masks[i]))
        return res

    def getMask(self, s):
        mask = 0
        for c in s:
            i = ord(c) - ord('a')
            if (mask & (1 << i)) != 0:
                return -1
            mask |= 1 << i
        return mask
  