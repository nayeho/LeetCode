class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        t = collections.Counter(target).most_common()
        a = collections.Counter(arr).most_common()
        t.sort()
        a.sort()
        return t == a
        