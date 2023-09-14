class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if k == n:
            return "0"

        dp = list(num)
        i, j = 0, 1
        while j < n:
            while dp[i] > dp[j] and k > 0:
                dp[i] = 'X'
                k -= 1

                while dp[i] == 'X' and i != 0:
                    i -= 1

                if i == 0 and dp[i] == 'X':
                    break

            j += 1
            i = j - 1

        j = n - 1
        while k > 0:
            if dp[j] != 'X':
                k -= 1
                dp[j] = 'X'
            else:
                j -= 1

        # print(dp)

        ans = ""
        for c in dp:
            if c != 'X':
                ans += c

        ans = ans.lstrip("0")
        if ans == "":
            return "0"

        return ans
