class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        a_state, b_state = 0, 0
        for i, c in enumerate(s):
            # print(a_state,b_state, s[:i])
            if c == "a":
                b_state = min(b_state+1, i+1-a_state)
            else:
                b_state = min(a_state, b_state)
                a_state += 1
        return min(a_state, b_state)
