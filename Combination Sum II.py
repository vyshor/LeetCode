class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = collections.Counter(candidates)
        dp = [[] for _ in range(target + 1)]
        dp[target] = [{k: 0 for k in counter.keys()}]
        candidates = list(set(counter.keys()))
        n = len(candidates)

        for i in range(n - 1, -1, -1):
            for j in range(target, -1, -1):
                if not dp[j]:
                    continue

                if j - candidates[i] < 0:
                    break

                for comb in dp[j]:
                    if comb[candidates[i]] < counter[candidates[i]]:
                        new_comb = dict(comb)
                        new_comb[candidates[i]] += 1
                        dp[j - candidates[i]].append(new_comb)

        ans = []
        for comb in dp[0]:
            order = []
            for k, i in comb.items():
                for _ in range(i):
                    order.append(k)
            ans.append(order)
        return ans


