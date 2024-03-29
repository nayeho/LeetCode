class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        prevOnes = 0

        for row in bank:
            ones = row.count('1')
            if ones:
                result += prevOnes * ones
                prevOnes = ones

        return result