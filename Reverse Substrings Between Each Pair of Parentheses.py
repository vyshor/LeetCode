class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)

        def reverse(i):
            window = ""
            while s[i] != ")":
                if s[i] == "(":
                    new_window, i = reverse(i+1)
                    window += new_window
                else:
                    window += s[i]
                    i += 1

            return window[::-1], i+1

        i = 0
        ans = ""
        while i < n:
            if s[i] == "(":
                rev, i = reverse(i+1)
                ans += rev
            else:
                ans += s[i]
                i += 1

        return ans
