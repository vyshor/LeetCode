class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        slices = 0
        if len(A) < 3:
            return 0
        start, end = 0, 1
        diff = A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                end += 1
            else:
                start = i-1
                end = i
                diff = A[i] - A[i-1]
            if (end - start + 1) >=3:
                slices += end - start - 1
        return slices

# Time: O(n)
# Space: O(1)

# Runtime: 40 ms, faster than 48.59% of Python3 online submissions for Arithmetic Slices.
# Memory Usage: 14.3 MB, less than 91.75% of Python3 online submissions for Arithmetic Slices.