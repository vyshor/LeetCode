class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            n = len(word)
            i, j = 0, n - 1
            palindrome = True
            while i < j:
                if word[i] == word[j]:
                    i += 1
                    j -= 1
                else:
                    palindrome = False
                    break
            if palindrome:
                return word
        return ""
