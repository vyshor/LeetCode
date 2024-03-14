class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        if goal == 0:
            combo = 0
            total = 0
            for num in nums:
                if num == 1 and combo > 0:
                    total += (combo * (combo + 1)) // 2
                    combo = 0
                elif num == 0:
                    combo += 1

            if combo > 0:
                total += (combo * (combo + 1)) // 2
            return total

        arr = []
        combo = 1
        for num in nums:
            if num == 1:
                arr.append(combo)
                combo = 1
            else:
                combo += 1

        arr.append(combo)
        left, right = 0, goal
        total = 0
        while right < len(arr):
            total += arr[right] * arr[left]
            right += 1
            left += 1
        return total
