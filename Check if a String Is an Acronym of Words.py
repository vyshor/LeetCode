class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        n = len(s)
        n_words = len(words)
        if n != n_words:
            return False

        for i in range(n):
            if s[i] != words[i][0]:
                return False

        return True
