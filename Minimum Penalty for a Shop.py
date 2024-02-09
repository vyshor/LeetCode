class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        openn = [0] * n
        closed = [0] * n

        openn[0] = int(customers[0] == 'N')
        closed[0] = 1 - openn[0]
        closing_time = 0

        for i in range(1, n):
            openn[i] = openn[i-1] + int(customers[i] == 'N')
            if openn[i-1] < closed[i-1]:
                closing_time = i
            closed[i] = min(closed[i-1], openn[i-1]) + int(customers[i] == 'Y')
        if openn[-1] < closed[-1]:
            closing_time = n

        # print(openn)
        # print(closed)
        return closing_time
