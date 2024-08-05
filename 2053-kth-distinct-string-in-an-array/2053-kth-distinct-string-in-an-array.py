class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = collections.Counter(arr)
        check = 0
        for letter, cnt in c.items():
            if cnt == 1:
                check += 1
            if check == k:
                return letter
        return ''
        