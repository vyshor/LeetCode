class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dp = {}
        i = 0
        for c in key:
            if c in dp or c == " ":
                continue

            dp[c] = i
            i += 1

        decoded = ""
        for c in message:
            if c == " ":
                decoded += " "
            else:
                decoded += chr(dp[c] + 97)
        return decoded
