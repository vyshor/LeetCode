class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        closest = sum(nums[:3])
        nums.sort()

        pt1 = 0

        while pt1 < n-1:
            pt2 = pt1 + 1
            pt3 = n-1
            while pt2 < pt3:
                total = nums[pt1] + nums[pt2] + nums[pt3]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total == target:
                    return closest
                elif total > target:
                    pt3 -= 1
                else:
                    pt2 += 1
            pt1 += 1

        return closest
