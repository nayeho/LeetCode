class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = 0
        net = 0
        summ = 0
        length = len(gas)

        for i in range(length):
            net += gas[i] - cost[i]
            summ += gas[i] - cost[i]
            if summ < 0:
                summ = 0
                result = i + 1

        return -1 if net < 0 else result
        
        