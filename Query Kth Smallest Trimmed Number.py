class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:

        n = len(queries)
        q = {}

        for i, query in enumerate(queries):
            (k, trim) = query
            if trim not in q:
                q[trim] = [(k, i)]
            else:
                q[trim].append((k, i))

        ans = [0] * n

        for trim, k_pairs in q.items():
            new_nums = [(num[-trim:], i) for i, num in enumerate(nums)]
            new_nums.sort()

            for (k, i) in k_pairs:
                ans[i] = new_nums[k - 1][1]

        return ans
