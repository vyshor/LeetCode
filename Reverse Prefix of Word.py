class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        for i, c in enumerate(word):
            stack.append(c)
            if ch == c:
                return "".join(stack[::-1]) + word[i+1:]
        return word
