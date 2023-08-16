class Solution:
    def reverseWords(self, s: str) -> str:
        rev = []
        for word in s.split(" "):
            if word:
                rev.append(word)
        return ' '.join(rev[::-1])