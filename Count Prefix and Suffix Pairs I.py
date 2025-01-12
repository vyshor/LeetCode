class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(wordA, wordB):
            if len(wordA) > len(wordB):
                return False
            n = len(wordA)
            return wordA == wordB[:n] and wordA == wordB[-n:]

        count = 0
        for i in range(len(words)):
            for j in range(i):
                count += int(isPrefixAndSuffix(words[j], words[i]))
        return count