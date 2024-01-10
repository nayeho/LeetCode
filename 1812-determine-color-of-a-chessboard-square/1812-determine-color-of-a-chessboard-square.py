class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        # print(ord('a'))
        
        # ord('a') -> 97
        # a1 -> 97 + 1 = 98(even) -> False
        
        return (ord(coordinates[0]) + int(coordinates[1])) % 2 == 1
        