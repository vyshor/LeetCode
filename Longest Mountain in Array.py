class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        if n < 3:
            return 0

        maxSize = 0
        start = 0
        prev = arr[0]
        up = True

        for i in range(1, n):
            if prev == arr[i]:
                if i - start >= 3 and not up:
                    maxSize = max(maxSize, i - start)
                start = i
            elif prev < arr[i]:
                if not up:
                    if i - start >= 3:
                        maxSize = max(maxSize, i - start)
                    start = i - 1
                    up = True
            else:
                if up:
                    up = False
                    if i - start <= 1:
                        start = i
                        up = True

            # print(prev, arr[i],up, start, maxSize )
            prev = arr[i]

        if n - start >= 3 and not up:
            maxSize = max(maxSize, n - start)
        return maxSize


