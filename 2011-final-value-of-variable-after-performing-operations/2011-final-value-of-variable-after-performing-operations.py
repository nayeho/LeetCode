class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        
        result = 0
        
        c = Counter(operations)
        result += c['X++'] + c['++X'] - c['X--'] - c['--X']
        
        return result
        