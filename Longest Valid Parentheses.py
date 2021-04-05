class Solution:
    def longestValidParentheses(self, s: str) -> int:
        valid = [0] * len(s)
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if len(stack):
                    valid[stack.pop()] = 1
                    valid[i] = 1

        ans = 0
        window = 0
        for i in valid:
            if i:
                window += 1
                ans = max(window, ans)
            else:
                window = 0
        return ans

# Time: O(n)
# Space: O(n)

# Runtime: 48 ms, faster than 44.29% of Python3 online submissions for Longest Valid Parentheses.
# Memory Usage: 14.8 MB, less than 24.35% of Python3 online submissions for Longest Valid Parentheses.
