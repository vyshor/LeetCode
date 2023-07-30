class Solution:
    dp = {}

    def RecurGetMaxMin(self, nums, start, end, maxxTurn) -> (int, int):
        dp = self.dp

        if (start, end) in dp:
            return dp[(start, end)]

        if start == end:
            maxx, minn = 0, 0
            if maxxTurn:
                maxx += nums[start]
            else:
                minn += nums[start]
            dp[(start, end)] = maxx, minn
            return maxx, minn

        if maxxTurn:
            # Pick start index
            num = nums[start]
            startMaxx, startMinn = self.RecurGetMaxMin(nums, start + 1, end, not maxxTurn)
            startMaxx += num

            # Pick end index
            num = nums[end]
            endMaxx, endMinn = self.RecurGetMaxMin(nums, start, end - 1, not maxxTurn)
            endMaxx += num

            if startMaxx - startMinn >= endMaxx - endMinn:
                dp[(start, end)] = startMaxx, startMinn
                return startMaxx, startMinn
            else:
                dp[(start, end)] = endMaxx, endMinn
                return endMaxx, endMinn
        else:
            # Pick start index
            num = nums[start]
            startMaxx, startMinn = self.RecurGetMaxMin(nums, start + 1, end, not maxxTurn)
            startMinn += num

            # Pick end index
            num = nums[end]
            endMaxx, endMinn = self.RecurGetMaxMin(nums, start, end - 1, not maxxTurn)
            endMinn += num

            if startMinn - startMaxx >= endMinn - endMaxx:
                dp[(start, end)] = startMaxx, startMinn
                return startMaxx, startMinn
            else:
                dp[(start, end)] = endMaxx, endMinn
                return endMaxx, endMinn

    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.dp = {}
        start, end = 0, len(nums) - 1
        maxx, minn = self.RecurGetMaxMin(nums, start, end, True)
        return maxx >= minn
