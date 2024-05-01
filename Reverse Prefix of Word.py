class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        i = word.find(ch)
        if i == -1:
            return word
        return word[i::-1] + word[i+1:]
# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         stack = []
#         for i, c in enumerate(word):
#             stack.append(c)
#             if ch == c:
#                 return "".join(stack[::-1]) + word[i+1:]
#         return word
