class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        carry_over = 0
        steps = 0
        i = n-1
        while i > 0:
            # print(i, steps, carry_over)
            if (s[i] == "1" and carry_over == 0) or (s[i] == "0" and carry_over):
                steps += 2
                carry_over = 1
            else:
                steps += 1
                carry_over = int(s[i] == "1")
            i -= 1
        # print(i, steps, carry_over)
        return steps + carry_over
