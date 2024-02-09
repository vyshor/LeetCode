class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        n = len(s)
        counter = Counter(s)
        unique = len(counter)
        maxx = 0

        for j in range(1, unique + 1):
            left, right = 0, 0
            counter = {}
            while right < n:
                if s[right] not in counter:
                    counter[s[right]] = 1
                else:
                    counter[s[right]] += 1

                while len(counter) > j and left < right:
                    counter[s[left]] -= 1
                    if counter[s[left]] == 0:
                        del counter[s[left]]
                    left += 1

                if len(counter) == j and all([v >= k for v in counter.values()]):
                    maxx = max(maxx, right - left + 1)

                right += 1

        return maxx
