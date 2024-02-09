class Solution:
    def reverseWords(self, s: str) -> str:
        word = []
        ans = ""
        for c in s:
            if c == " ":
                if word:
                    ans += "".join(word[::-1])
                    word = []

                ans += " "
            else:
                word.append(c)

        if word:
            ans += "".join(word[::-1])

        return ans
