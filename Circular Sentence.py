class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split()
        n = len(words)
        for i in range(1, n):
            if words[i][0] != words[i-1][-1]:
                return False
        return words[-1][-1] == words[0][0]
