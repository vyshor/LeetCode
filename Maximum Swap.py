class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))
        n = len(nums)
        prev = nums[0]
        i = 1
        spot = 0
        found = False
        maxx = 0
        j = 0
        while i < n:
            if not found:
                if nums[i] > nums[i - 1]:
                    found = True
                    maxx = nums[i]
                    j = i
                elif nums[i] < nums[i - 1]:
                    spot = i
            else:
                if nums[i] >= maxx:
                    maxx = nums[i]
                    j = i
            i += 1

        # print(spot, j)
        if found:
            i = 0
            while i < spot:
                if nums[i] < maxx:
                    spot = i
                i += 1
            nums[spot], nums[j] = nums[j], nums[spot]
        else:
            return num
        return int(''.join(nums))
