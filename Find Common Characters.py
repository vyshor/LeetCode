class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        def count(word):
            counter = [0] * 26
            for c in word:
                counter[ord(c) - 97] += 1
            return counter

        counter = count(words[0])
        n = len(words)
        for i in range(1, n):
            counter2 = count(words[i])
            for j in range(26):
                counter[j] = min(counter[j], counter2[j])
        ans = []
        for i, c in enumerate(counter):
            for _ in range(c):
                ans.append(chr(i + 97))
        return ans
