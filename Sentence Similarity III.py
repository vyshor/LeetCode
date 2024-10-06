class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        splits1 = sentence1.split()
        splits2 = sentence2.split()
        if len(splits1) > len(splits2):
            splits1, splits2 = splits2, splits1

        n1, n2 = len(splits1), len(splits2)
        if n1 == 1:
            return splits2[0] == splits1[0] or splits2[-1] == splits1[0]

        l1, r1 = 0, n1 - 1
        r2 = n2 - 1
        while l1 < n1 and splits1[l1] == splits2[l1]:
            l1 += 1
        while r1 >= l1 and splits1[r1] == splits2[r2]:
            r1 -= 1
            r2 -= 1
        # print(l1, r1, r2)
        return r1 < l1


