class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        counter = Counter(candidates)
        row = list(counter.keys())
        total = target
        n = len(row)
        ans = []
        curr = []
        # print(row)

        def explore(i):
            nonlocal counter, row, total, n, ans, curr
            if i == n:
                return

            num = row[i]
            # print(i, num)
            for j in range(counter[num]+1):
                total -= num * j
                if total < 0:
                    total += num * j
                    continue

                for _ in range(j):
                    curr.append(num)
                if total == 0:
                    ans.append(list(curr))
                    total += num * j
                    for _ in range(j):
                        curr.pop()
                    continue

                explore(i+1)
                for _ in range(j):
                    curr.pop()

                total += num * j
                # print(curr)
        explore(0)
        return ans

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         counter = collections.Counter(candidates)
#         dp = [[] for _ in range(target + 1)]
#         dp[target] = [{k: 0 for k in counter.keys()}]
#         candidates = list(set(counter.keys()))
#         n = len(candidates)
#
#         for i in range(n - 1, -1, -1):
#             for j in range(target, -1, -1):
#                 if not dp[j]:
#                     continue
#
#                 if j - candidates[i] < 0:
#                     break
#
#                 for comb in dp[j]:
#                     if comb[candidates[i]] < counter[candidates[i]]:
#                         new_comb = dict(comb)
#                         new_comb[candidates[i]] += 1
#                         dp[j - candidates[i]].append(new_comb)
#
#         ans = []
#         for comb in dp[0]:
#             order = []
#             for k, i in comb.items():
#                 for _ in range(i):
#                     order.append(k)
#             ans.append(order)
#         return ans


