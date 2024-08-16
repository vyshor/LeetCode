class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minn0, minn1, maxx0, maxx1 = float('inf'), float('inf'), float('-inf'), float('-inf')
        i0, i1, j0, j1 = 0, 0, 0, 0
        for i, arr in enumerate(arrays):
            if arr[0] < minn0:
                minn0, minn1 = arr[0], minn0
                i0, i1 = i, i0
            elif arr[0] < minn1:
                minn1 = arr[0]
                i1 = i

            if arr[-1] > maxx0:
                maxx0, maxx1 = arr[-1], maxx0
                j0, j1 = i, j0
            elif arr[-1] > maxx1:
                maxx1 = arr[-1]
                j1 = i

        # print(minn0, minn1)
        # print(maxx0, maxx1)
        if i0 == j0:
            return max(maxx0 - minn1, maxx1 - minn0)
        return maxx0 - minn0
