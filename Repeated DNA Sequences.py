class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n <= 10:
            return []

        dp = set(s[:10])
        ans = set()
        for i in range(10, n+1):
            window = s[i-10:i]
            if window not in dp:
                dp.add(window)
            else:
                ans.add(window)
        return ans
