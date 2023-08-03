# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
# class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length()

        def findTarget(start, end):
            if end - start <= 3:
                for i in range(start, end):
                    if mountain_arr.get(i) == target:
                        return i
                return -1

            mid = (start + end) // 2
            # print(start, end, mid)

            mid_prev = mountain_arr.get(mid - 1)
            mid_val = mountain_arr.get(mid)
            mid_next = mountain_arr.get(mid + 1)
            if mid_prev < mid_val > mid_next:
                if mid_val == target:
                    return mid
                elif mid_val < target:
                    return -1
                else:
                    prev_find = findTarget(start, mid)
                    if prev_find != -1:
                        return prev_find

                    for i, val in enumerate([mid_prev, mid_val, mid_next]):
                        if val == target:
                            return mid - 1 + i

                    return findTarget(mid + 2, end)
            elif mid_prev < mid_val < mid_next:
                if target < mid_prev:
                    prev_find = findTarget(start, mid)
                    if prev_find != -1:
                        return prev_find
                elif target > mid_next:
                    return findTarget(mid + 2, end)

                for i, val in enumerate([mid_prev, mid_val, mid_next]):
                    if val == target:
                        return mid - 1 + i

                return findTarget(mid + 2, end)
            else:
                if target > mid_prev:
                    return findTarget(start, mid - 1)
                if target < mid_prev:
                    prev_find = findTarget(start, mid - 1)
                    if prev_find != -1:
                        return prev_find
                if target < mid_next:
                    next_find = findTarget(mid + 2, end)
                    if next_find != -1:
                        return next_find

                for i, val in enumerate([mid_prev, mid_val, mid_next]):
                    if val == target:
                        return mid - 1 + i
                return -1

        return findTarget(0, n)
