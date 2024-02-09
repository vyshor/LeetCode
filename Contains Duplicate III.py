class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        n = len(nums)
        arr = sorted([(num, i) for i, num in enumerate(nums)])
        # print(arr)

        for i in range(n):
            num = nums[i]
            leftTarget = num - valueDiff
            rightTarget = num + valueDiff
            left = bisect.bisect_right(arr, (leftTarget, -1))
            right = bisect.bisect_left(arr, (rightTarget, n))

            # print(left, right)

            for j in range(left, right):
                _, k = arr[j]
                if k != i and abs(k - i) <= indexDiff:
                    # print(k, i)
                    return True

        return False
