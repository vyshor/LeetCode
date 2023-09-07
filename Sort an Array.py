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

# class Solution:
#     def sortArray(self, nums: List[int]) -> List[int]:
#         def quickSort(start, end):
#             if start >= end:
#                 return
#
#             partition = end
#             i, j = start, start
#             while i < end:
#                 if nums[i] < nums[partition]:
#                     nums[i], nums[j] = nums[j], nums[i]
#                     j += 1
#                     i += 1
#                 else:
#                     i += 1
#             nums[j], nums[partition] = nums[partition], nums[j]
#
#             # print(i, j)
#             # print(nums)
#
#             quickSort(start, j - 1)
#             quickSort(j + 1, end)
#
#         quickSort(0, len(nums) - 1)
#         return nums
