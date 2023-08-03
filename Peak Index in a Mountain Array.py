class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        def findPeak(start, end):
            if end - start <= 3:
                m = max(arr[start:end])
                return start + arr[start:end].index(m)

            mid = (start + end) // 2
            if arr[mid - 1] < arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid - 1] < arr[mid] < arr[mid + 1]:
                return findPeak(mid, end)
            else:
                return findPeak(start, mid + 1)

        return findPeak(0, len(arr))
