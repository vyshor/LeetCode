class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = list(set(arr2))
        arr2.sort()

        n = len(arr1)
        n2 = len(arr2)

        dp = {}

        def exploreIndex(i, prev_num):
            if i == n:
                return 0

            if (i, prev_num) in dp:
                return dp[(i, prev_num)]

            minOps = float('inf')
            if arr1[i] > prev_num:
                minOps = min(minOps, exploreIndex(i + 1, arr1[i]))

            j = bisect.bisect_right(arr2, prev_num)
            if j < n2 and arr2[j] > prev_num:
                minOps = min(minOps, exploreIndex(i + 1, arr2[j]) + 1)

            dp[(i, prev_num)] = minOps
            return dp[(i, prev_num)]

        ans = min(exploreIndex(1, arr1[0]), exploreIndex(1, arr2[0]) + 1)
        if ans == float('inf'):
            return -1
        return ans
