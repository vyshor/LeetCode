class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ranks = [0] * n
        order = sorted([(num, i) for i, num in enumerate(arr)])
        k = 1
        prev = float('-inf')
        for i in range(n):
            num, j = order[i]
            if num == prev:
                ranks[j] = k-1
            else:
                ranks[j] = k
                k += 1
            prev = num
        return ranks
