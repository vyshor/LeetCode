class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        n = len(nums)
        left, right = 0, 0
        count = 0
        minn, maxx = nums[left], nums[left]
        min_i, max_i = 0, 0

        while right < n:
            # print(nums[right], left, right, minn, maxx, "Count:", count)
            if nums[right] > maxK or nums[right] < minK:
                # Reset the sliding window
                right += 1
                left = right
                if left < n:
                    minn, maxx = nums[left], nums[left]
                    min_i, max_i = left, left
            else:
                if nums[right] == minK:
                    min_i = right
                minn = min(minn, nums[right])
                if nums[right] == maxK:
                    max_i = right
                maxx = max(maxx, nums[right])

                if minn == minK and maxx == maxK:
                    # print("Min_i", min_i, "Max_i", max_i)
                    count += min(min_i, max_i) - left + 1
                right += 1
        return count

