class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1

        start, end, jump = 1, n, 1
        while start < end:
            # print(start, end)

            # Forward jump

            if (end - start) % (2 * jump) == 0:
                end -= jump
            start += jump
            jump *= 2

            if start == end:
                break

            # Backward jump
            if (end - start) % (2 * jump) == 0:
                start += jump
            end -= jump
            jump *= 2

        return start
