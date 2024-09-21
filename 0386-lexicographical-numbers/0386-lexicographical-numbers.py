class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        result = []
        check = 1

        while len(result) < n:
            result.append(check)
            if check * 10 <= n:
                check *= 10
            else:
                while check % 10 == 9 or check == n:
                    check //= 10
                check += 1

        return result