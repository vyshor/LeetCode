class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def diff(a, b):
            n = len(a)
            diff_count = 0
            for i in range(n):
                diff_count += int(a[i] != b[i])
            return diff_count

        arr = []
        for q in queries:
            for word in dictionary:
                if diff(q, word) <= 2:
                    arr.append(q)
                    break

        return arr
