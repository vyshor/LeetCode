class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        start, end = 0, n - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
