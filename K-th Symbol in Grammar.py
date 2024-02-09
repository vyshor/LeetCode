class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        flips = 0
        arr_size = 2**(n-1)
        while arr_size > 1:
            next_arr_size = arr_size // 2
            if k > next_arr_size:
                flips += 1
                k = k - next_arr_size
            arr_size = next_arr_size
        # print(flips)
        return flips % 2
