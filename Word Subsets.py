from collections import Counter
class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        dp = {}
        for word in B:
            for add_char, count in dict(Counter(word)).items():
                if add_char in dp:
                    dp[add_char] = max(count, dp[add_char])
                else:
                    dp[add_char] = count

        ans = []
        for word in A:
            word_dict = Counter(word)
            add_word = True
            for c, count in dp.items():
                if c not in word_dict or count > word_dict[c]:
                    add_word = False
                    break
            if add_word:
                ans.append(word)
        return ans

# Time: O(Nn+Mm) , where n for max length of word in A, N for number of words in A, m for max length of word in B, M for number of words in B.
# Space: O(Mm)

# Runtime: 808 ms, faster than 68.99% of Python3 online submissions for Word Subsets.
# Memory Usage: 17.8 MB, less than 98.06% of Python3 online submissions for Word Subsets.
