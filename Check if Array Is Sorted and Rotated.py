class Solution:
    def check(self, nums: List[int]) -> bool:
        use_rotates = False
        n = len(nums)
        if nums[n-1] > nums[0]:
            use_rotates = True

        for i in range(1, n):
            if nums[i-1] > nums[i]:
                if use_rotates:
                    return False
                else:
                    use_rotates = True
        return True
