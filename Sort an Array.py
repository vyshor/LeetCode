class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def recurSort(arr):
            n = len(arr)
            if n <= 1:
                return arr
            mid = n // 2
            arrA, arrB = recurSort(arr[:mid]), recurSort(arr[mid:])
            return mergeArr(arrA, arrB)

        def mergeArr(arrA, arrB):
            nA, nB = len(arrA), len(arrB)
            ptA, ptB = 0, 0
            merged = []
            while ptA < nA and ptB < nB:
                if arrA[ptA] < arrB[ptB]:
                    merged.append(arrA[ptA])
                    ptA += 1
                else:
                    merged.append(arrB[ptB])
                    ptB += 1

            if ptA < nA:
                merged += arrA[ptA:]
            if ptB < nB:
                merged += arrB[ptB:]

            return merged

        return recurSort(nums)
