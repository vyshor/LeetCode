class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        losses, gains = [], []
        for cost, cashback in transactions:
            nett_gain = cashback - cost
            if nett_gain > 0:
                gains.append((-cost))
            else:
                losses.append((cashback, -cost, -cost + cashback))

        losses.sort()
        heapq.heapify(gains)

        if not gains:
            gains = [0]

        # The more negative the nett_gain the earlier
        # The larger the cashback the later it should be

        minn = 0
        net_state = 0

        for (_, cost, nett_gain) in losses:
            minn = min(minn, net_state + cost)
            net_state += nett_gain

        return -min(minn, net_state + gains[0])
