class Solution:
    def minimumSteps(self, s: str) -> int:
        count = 0
        n = len(s)
        left, right = 0, 0
        while right < n:
            # print(left, right)
            if s[right] == "0":
                count += right-left
                left += 1
            right += 1
        return count
