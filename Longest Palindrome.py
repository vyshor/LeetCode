class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        even_count = 0
        counter = Counter()
        for c in s:
            counter[c] += 1
            if counter[c] % 2 == 0:
                even_count += 1
                odd_count -= 1
            else:
                odd_count += 1
        return even_count * 2 + (1 if odd_count else 0)


