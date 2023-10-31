class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, 1
        summ = nums[left]
        window = {nums[left]: 1}
        maxx = 0

        if right - left == k:
            maxx = max(maxx, summ)

        while right < n:
            # print(left, right, summ, window)

            summ += nums[right]
            if nums[right] in window:
                window[nums[right]] += 1
            else:
                window[nums[right]] = 1

            while left < right and (right - left + 1 > k or window[nums[right]] > 1):
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]

                summ -= nums[left]
                left += 1

            if right - left + 1 == k:
                maxx = max(maxx, summ)

            right += 1

        return maxx
