class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pop_idx = 0
        for pu in pushed:
            stack.append(pu)
            while stack and stack[-1] == popped[pop_idx]:
                stack.pop()
                pop_idx += 1
        return not stack

# Time: O(n)
# Space: O(n)

# Runtime: 72 ms, faster than 63.35% of Python3 online submissions for Validate Stack Sequences.
# Memory Usage: 14.5 MB, less than 61.37% of Python3 online submissions for Validate Stack Sequences.