class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = [0] * n
        left, right = 0, n - 1

        def mergeArray(a, b):
            nonlocal dp, nums

            na, nb = len(a), len(b)
            i, j = 0, 0
            merged = []
            b_count = 0

            while i < na and j < nb:
                if nums[a[i]] <= nums[b[j]]:
                    merged.append(a[i])
                    dp[a[i]] += b_count
                    i += 1
                else:
                    merged.append(b[j])
                    b_count += 1
                    j += 1

            while i < na:
                merged.append(a[i])
                dp[a[i]] += b_count
                i += 1

            while j < nb:
                merged.append(b[j])
                j += 1

            return merged

        def splitArray(left, right):
            if left > right:
                return []

            if left == right:
                return [left]

            mid = (left + right) // 2
            leftSplit = splitArray(left, mid)
            rightSplit = splitArray(mid + 1, right)

            return mergeArray(leftSplit, rightSplit)

        splitArray(left, right)
        return dp

# class Solution:
#     def countSmaller(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         dp = [0] * n
#         q = []
#
#         for i in range(n - 1, -1, -1):
#             dp[i] = bisect.bisect_left(q, nums[i])
#             q.insert(dp[i], nums[i])
#
#         return dp
