class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        result = []
        
        for i, op in enumerate(operations):
            if op == 'C':
                result.pop(-1)
            elif op == 'D':
                result.append(result[-1] * 2)
            elif op == '+':
                result.append(result[-1] + result[-2])
            else:
                result.append(int(op))
                
        return sum(result)
        