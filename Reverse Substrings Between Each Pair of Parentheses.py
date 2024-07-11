class Solution:
    def reverseParentheses(self, s: str) -> str:
        def accumulate(i, n):
            arr = []
            while 1:
                if i >= n:
                    return arr, i

                if s[i] == ")":
                    return arr[::-1], i + 1

                if s[i] == "(":
                    arr2, j = accumulate(i + 1, n)
                    arr += arr2
                    i = j
                    continue

                arr.append(s[i])
                i += 1

        arr, _ = accumulate(0, len(s))
        return ''.join(arr)

# class Solution:
#     def reverseParentheses(self, s: str) -> str:
#         n = len(s)
#
#         def reverse(i):
#             window = ""
#             while s[i] != ")":
#                 if s[i] == "(":
#                     new_window, i = reverse(i+1)
#                     window += new_window
#                 else:
#                     window += s[i]
#                     i += 1
#
#             return window[::-1], i+1
#
#         i = 0
#         ans = ""
#         while i < n:
#             if s[i] == "(":
#                 rev, i = reverse(i+1)
#                 ans += rev
#             else:
#                 ans += s[i]
#                 i += 1
#
#         return ans
