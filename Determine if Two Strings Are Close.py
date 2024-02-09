class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        freq = {}
        if set(counter1.keys()) != set(counter2.keys()):
            return False

        for count in counter1.values():
            if count not in freq:
                freq[count] = 1
            else:
                freq[count] += 1

        for count in counter2.values():
            if count not in freq:
                return False
            else:
                freq[count] -= 1
                if freq[count] == 0:
                    del freq[count]
        return True

# from collections import Counter
#
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         c1 = Counter(word1)
#         c2 = Counter(word2)
#         return set(c1.keys()) == set(c2.keys()) and sorted(c1.values()) == sorted(c2.values())

# Runtime: 136 ms, faster than 76.39% of Python3 online submissions for Determine if Two Strings Are Close.
# Memory Usage: 15.5 MB, less than 27.70% of Python3 online submissions for Determine if Two Strings Are Close.

# Time: O(n+m)
# Space: O(n+m)