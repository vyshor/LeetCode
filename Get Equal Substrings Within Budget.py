class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left, right = 0, 0
        costs = []
        n = len(s)
        cost = 0
        maxx = 0
        while right < n:
            costs.append(abs(ord(s[right]) - ord(t[right])))
            cost += costs[right]

            while cost > maxCost:
                cost -= costs[left]
                left += 1

            right += 1
            maxx = max(maxx, right-left)
        return maxx
