class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = [{} for _ in range(k)]
        for num in nums:
            if num not in counter[num % k]:
                counter[num % k][num] = 1
            else:
                counter[num % k][num] += 1

        ans = 1
        for i in range(k):
            prev, state0, state1 = 0, 1, 0
            for j in sorted(counter[i].keys()):
                j_count = 2 ** counter[i][j]
                if prev + k == j:
                    state0, state1 = state0 + state1, state0 * (j_count - 1)
                else:
                    state0, state1 = state0 + state1, (state0 + state1) * (j_count - 1)
                prev = j
            ans *= state0 + state1
        return ans - 1


# class Solution:
#     def beautifulSubsets(self, nums: List[int], k: int) -> int:
#         seen = {}
#         n = len(nums)
#         count = 0
#
#         def explore(i):
#             nonlocal seen, n, count
#             if i == n:
#                 if seen:
#                     count += 1
#                 return
#
#             explore(i + 1)
#
#             if nums[i] + k not in seen and nums[i] - k not in seen:
#                 if nums[i] in seen:
#                     seen[nums[i]] += 1
#                 else:
#                     seen[nums[i]] = 1
#
#                 explore(i + 1)
#                 seen[nums[i]] -= 1
#                 if seen[nums[i]] == 0:
#                     del seen[nums[i]]
#
#         explore(0)
#         return count
