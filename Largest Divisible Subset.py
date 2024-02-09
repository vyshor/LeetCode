class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = {}
        largest = 1
        subset = (nums[0], )
        for num in nums:
            maxx = 1
            maxx_pattern = (num, )
            for val, (count, pattern) in dp.items():
                if num % val == 0 and count+1 > maxx:
                    maxx = count+1
                    maxx_pattern = pattern + (num, )
            dp[num] = (maxx, maxx_pattern)
            if maxx > largest:
                largest = maxx
                subset = maxx_pattern
        return subset
