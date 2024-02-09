class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        order = [(pos, i) for i, pos in enumerate(position)]
        order.sort()

        prev_t = float('-inf')
        count = 0

        for i in range(n - 1, -1, -1):
            pos, j = order[i]
            dist = target - pos
            t = dist / speed[j]

            # If car behind takes longer time,
            # Then it will create a new fleet
            if t > prev_t:
                count += 1
                prev_t = t
            # If car behind takes a shorter time,
            # it will merge with existing fleet

        return count
