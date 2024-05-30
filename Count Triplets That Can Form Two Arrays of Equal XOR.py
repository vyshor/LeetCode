class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        dp = {}
        count = 0
        for i in range(n):
            current_xor = 0
            for j in range(i, n):
                current_xor ^= arr[j]
                if (current_xor, i-1) in dp:
                    count += dp[(current_xor, i-1)]

                if (current_xor, j) not in dp:
                    dp[(current_xor, j)] = 1
                else:
                    dp[(current_xor, j)] += 1
        return count
