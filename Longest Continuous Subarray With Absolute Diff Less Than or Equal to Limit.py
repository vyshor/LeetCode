class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        counter = {}
        minn, maxx = [], []
        left, right = 0, 0
        count = 0
        while right < n:
            num = nums[right]
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

            heapq.heappush(minn, num)
            heapq.heappush(maxx, -num)

            while -maxx[0]-minn[0] > limit:
                num = nums[left]
                counter[num] -= 1
                while counter[-maxx[0]] == 0:
                    heapq.heappop(maxx)
                while counter[minn[0]] == 0:
                    heapq.heappop(minn)
                left += 1

            if -maxx[0]-minn[0] <= limit:
                count = max(count, right-left+1)

            right += 1
        return count
