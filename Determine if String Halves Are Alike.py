class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        vowels = set('aeiouAEIOU')
        count = 0
        for i in range(n):
            if s[i] in vowels:
                if i < n // 2:
                    count += 1
                else:
                    count -= 1
        return count == 0

# from collections import Counter
# class Solution:
#     def halvesAreAlike(self, s: str) -> bool:
#         vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
#         a_s, b_s = Counter(s[:len(s)//2]), Counter(s[len(s)//2:])
#         a_c, b_c = 0, 0
#         for c in a_s:
#             if c in vowels:
#                 a_c += a_s[c]
#         for c in b_s:
#             if c in vowels:
#                 b_c += b_s[c]
#         return a_c == b_c

# Time: O(n)
# Space: O(1)

# Runtime: 28 ms, faster than 93.27% of Python3 online submissions for Determine if String Halves Are Alike.
# Memory Usage: 14.2 MB, less than 88.25% of Python3 online submissions for Determine if String Halves Are Alike.
