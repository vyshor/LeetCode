class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        n = len(s)
        left, right = 0, n - 1
        while True:
            while left < n and not s[left].isalpha():
                left += 1

            while right > 0 and not s[right].isalpha():
                right -= 1

            if left > right:
                break

            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return "".join(s)
