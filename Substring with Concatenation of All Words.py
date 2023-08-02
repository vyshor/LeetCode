class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = set()
        n = len(s)
        wordlen = len(words[0])
        num_words = len(words)
        wordslen = wordlen * num_words
        target = dict(Counter(words))

        for i in range(n-wordslen+1):
            counter = {k: 0 for k in target.keys()}
            for j in range(num_words):
                word = s[i+j*wordlen:i+(j+1)*wordlen]
                if word not in counter:
                    break

                counter[word] += 1
                if counter[word] > target[word]:
                    break
                if counter == target:
                    ans.add(i)

        return ans

# n = len(s)
# m = len(words)
# w = len(words[0])
# O(n*m)

