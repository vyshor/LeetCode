class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def coinMinus(remain_lst, remain_amt):

            val = remain_lst[0]
            if remain_amt % val == 0:
                return remain_amt // val
            else:
                if len(remain_lst) == 1:
                    return -1
                for i in range(remain_amt // val, -1, -1):
                    pos_outcome = coinMinus(remain_lst[1:], remain_amt - i * val)
                    if pos_outcome >= 0:
                        print(f"Coin Deno: {val}")
                        print(f"Remaining val: {remain_amt - i * val}")
                        print(f"Current coin count: {i + pos_outcome}")
                        return i + pos_outcome
                    else:
                        continue
            return -1
                
        # Depth first search so that it allows early termination
        coins.sort(reverse=True) # Most to least
        print(coins)
        return coinMinus(coins, amount)
            