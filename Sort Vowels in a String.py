class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set('aeiouAEIOU')
        arr = list(s)
        letters = []
        pos = []
        for i, c in enumerate(s):
            if c in vowels:
                letters.append(c)
                pos.append(i)

        letters.sort()
        for i, j in enumerate(pos):
            arr[j] = letters[i]

        return ''.join(arr)
