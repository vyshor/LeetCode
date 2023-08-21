class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        dp = {}

        def generateLps(word):
            nw = len(word)
            if nw == 1:
                return [0]

            lps = [0] * nw
            i, j = 0, 1
            while j < nw:
                if word[i] == word[j]:
                    lps[j] = i + 1
                    j += 1
                    i += 1
                else:
                    if i > 0:
                        i = lps[i - 1]
                    else:
                        j += 1
            return lps

        def compareStr(long, short, lps):
            l, s = len(long), len(short)
            i, j = 0, 0
            while i < l:
                if long[i] == short[j]:
                    i += 1
                    j += 1

                    if j == s:
                        return True
                else:
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return False

        for word in words:
            wordlen = len(word)
            if wordlen not in dp:
                dp[wordlen] = [(word, generateLps(word))]
            else:
                dp[wordlen].append((word, generateLps(word)))

        # print(dp)
        ans = set()
        for word in words:
            wordlen = len(word)
            for l, pairs in dp.items():
                if l <= wordlen:
                    for pair in pairs:
                        compare_word, lps = pair
                        if compare_word == word:
                            continue
                        if compareStr(word, compare_word, lps):
                            ans.add(compare_word)
        return list(ans)

