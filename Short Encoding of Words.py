class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words_set = set([''.join(reversed(word)) for word in words])
        letters_count = [(len(word), ''.join(reversed(word))) for word in words]
        letters_count.sort(reverse=True)
        total_required = 0
        for (count, word) in letters_count:
            if word in words_set:
                for i in range(len(word)):
                    if word[:i+1] in words_set:
                        words_set.remove(word[:i+1])
                total_required += count+1
        return total_required

# Time: O(nm) n number of words, m for max length of word
# Space: O(nm)

# Runtime: 164 ms, faster than 50.58% of Python3 online submissions for Short Encoding of Words.
# Memory Usage: 14.8 MB, less than 96.51% of Python3 online submissions for Short Encoding of Words.
