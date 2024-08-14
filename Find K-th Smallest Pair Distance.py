class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        nums = list(counter.keys())
        nums.sort()

        n = len(nums)
        q = []

        for i in range(n):
            if counter[nums[i]] > 1:
                k -= (counter[nums[i]] * (counter[nums[i]] - 1)) // 2

        if k <= 1:
            return 0

        def check(window):
            left = 0
            limit = nums[left] + window
            i = left + 1
            count = 0
            while i < n and nums[i] <= limit:
                count += counter[nums[i]]
                i += 1
            total = counter[nums[left]] * count

            while left < n - 1:
                # print(i, total, count)
                if k <= total:
                    return True
                left += 1
                count -= counter[nums[left]]
                limit = nums[left] + window
                while i < n and nums[i] <= limit:
                    count += counter[nums[i]]
                    i += 1
                total += counter[nums[left]] * count
            return k <= total

        minn, maxx = 1, nums[-1] - nums[0]
        while minn < maxx:
            mid = (minn + maxx) // 2
            left_side = check(mid)
            # print(minn, mid, maxx, left_side)
            if left_side:
                maxx = mid
            else:
                minn = mid + 1
        return minn
