class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            elif len(stack) < 1 or stack.pop() != pair[c]:
                return False
        return len(stack) == 0

# Runtime: 32 ms, faster than 63.20% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.4 MB, less than 8.34% of Python3 online submissions for Valid Parentheses.

# Time: O(n)
# Space: O(n)


class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        matching = {
            '{' : '}',
            '(' : ')',
            '[': ']'
        }
        for c in s:
            if c in ['(', '{', '[']:
                l.append(c)
            else:
                if not l or c != matching[l.pop()]:
                    return False
        if not l:
            return True
        else:
            return False

# Time: O(n)
# Space: O(n)
# Runtime: 28 ms, faster than 98.93% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.