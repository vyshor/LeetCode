class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        dp = [0] * k
        for num in arr:
            dp[(num % k)] += 1
        # print(dp)
        if dp[0] % 2 == 1:
            return False
        i = 1
        j = len(dp)-1
        while i < j:
            if dp[i] != dp[j]:
                return False
            i += 1
            j -= 1
        if i == j:
            if dp[i] % 2 == 1:
                return False
        return True
