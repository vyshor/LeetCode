class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = -1
        score = 0
        closed = True
        for c in S:
            if c == "(":
                stack += 1
                closed = False
            else:
                if not closed:
                    score += 2 ** stack
                    closed = True
                stack -= 1
        return score

# Time: O(n)
# Space: O(1)

# Runtime: 28 ms, faster than 83.50% of Python3 online submissions for Score of Parentheses.
# Memory Usage: 14 MB, less than 89.68% of Python3 online submissions for Score of Parentheses.