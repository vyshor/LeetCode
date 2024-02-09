class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        q = []
        for (birth, death) in logs:
            q.append((birth, 1))
            q.append((death, -1))

        q.sort()
        maxx = float('-inf')
        maxx_year = 0
        count = 0
        i = 0
        n = len(q)
        for i in range(n):
            year, increase = q[i]
            count += increase
            if count > maxx and (i+1 >= n or q[i+1][0] > year):
                maxx_year = year
                maxx = count
        return maxx_year
