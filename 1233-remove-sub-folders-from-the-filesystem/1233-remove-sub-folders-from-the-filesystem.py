class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        result = []
        prev = ''

        folder.sort()

        for f in folder:
            if len(prev) > 0 and f.startswith(prev) and f[len(prev)] == '/':
                continue
            result.append(f)
            prev = f

        return result