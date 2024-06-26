class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        removed = set()
        for i, c in enumerate(s):
            if c == ")":
                if not stack:
                    removed.add(i)
                else:
                    stack.pop()
            elif c == "(":
                stack.append(i)

        removed |= set(stack)
        new_str = []
        for i, c in enumerate(s):
            if i not in removed:
                new_str.append(c)
        return ''.join(new_str)

# class Solution:
#     def minRemoveToMakeValid(self, s: str) -> str:
#         stack = []
#         to_remove = set()
#         for idx, c in enumerate(s):
#             if c == "(":
#                 stack.append(("(", idx))
#             elif c == ")":
#                 if len(stack) == 0:
#                     to_remove.add(idx)
#                 else:
#                     stack.pop()
#         to_remove = to_remove.union([i[1] for i in stack])
#         ans = ""
#         for idx, c in enumerate(s):
#             if idx not in to_remove:
#                 ans += c
#         return ans

# Time: O(n)
# Space: O(n)

# Runtime: 124 ms, faster than 61.81% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
# Memory Usage: 16.3 MB, less than 26.54% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.
