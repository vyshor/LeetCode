class Solution:
    def reverseVowels(self, s: str) -> str:
        v = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        stack = []
        for c in s:
            if c in v:
                stack.append(c)

        rev = ""
        for c in s:
            if c in v:
                rev += stack.pop()
            else:
                rev += c
        return rev
