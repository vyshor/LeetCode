class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        nett = [0] * n
        nett_sum = 0

        for i in range(n):
            nett[i] = gas[i] - cost[i]
            nett_sum += nett[i]

        if nett_sum < 0:
            return -1

        start = 0
        nett_sum = 0
        for i in range(n):
            if nett_sum < 0:
                start = i
                nett_sum = 0

            nett_sum += nett[i]

        return start
