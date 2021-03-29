from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        words = ["zero", "six", "two", "four", "three", "eight", "five",
                 "seven", "one", "nine"]
        nums = "0624385719"
        words = [Counter(word) for word in words]
        c = Counter(s)
        ans = ''
        for idx, word in enumerate(words):
            repeat = 99999
            next_word = False
            for char, count in word.items():
                if char not in c:
                    next_word = True
                    break
                else:
                    repeat = min(c[char] // count, repeat)
            if not next_word:
                for char, count in word.items():
                    c[char] -= repeat * count
                ans += nums[idx] * repeat
        return ''.join(sorted(ans))

# Time: O(n)
# Space: O(n)

# Runtime: 44 ms, faster than 86.90% of Python3 online submissions for Reconstruct Original Digits from English.
# Memory Usage: 14.4 MB, less than 93.45% of Python3 online submissions for Reconstruct Original Digits from English.
