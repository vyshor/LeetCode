class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        q = [()]
        ans = []

        for i in range(1, n + 1):
            new_q = list(q)
            for comb in q:
                new_comb = comb + (i,)
                if len(new_comb) == k:
                    ans.append(new_comb)
                else:
                    new_q.append(new_comb)
            q = new_q

        return ans

