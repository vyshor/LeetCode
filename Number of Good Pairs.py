class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        ans = 0
        for count in counter.values():
            ans += count * (count - 1) // 2
        return ans
