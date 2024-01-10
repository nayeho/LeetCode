class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low == high:
            return 1 if low % 2 == 1 else 0
        
        # case 1 : low = 3, high = 7 -> 3, 5, 7 -> 3 // 4
        # case 2 : low = 2, high = 7 -> 3, 5, 7 -> 3 // 5
        # case 3 : low = 3, high = 8 -> 3, 5, 7 -> 3 // 5
        # case 4 : low = 2, high = 8 -> 3, 5, 7 -> 3 // 6
        
        if low % 2 == 1:
            return (high - low) // 2 + 1
        else:
            return (high - low + 1) // 2
