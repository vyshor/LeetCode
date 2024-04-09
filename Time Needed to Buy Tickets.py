class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        pass_k = False
        total = 0
        for i in range(n):
            if not pass_k:
                total += min(tickets[i], tickets[k])
            else:
                total += min(tickets[i], tickets[k] - 1)

            if i == k:
                pass_k = True
        return total
