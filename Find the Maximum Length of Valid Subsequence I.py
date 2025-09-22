class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_start_alt = 0
        even_start_alt = 1
        odd_start_const = 0
        even_start_const = 0
        for num in nums:
            odd_start_alt += (odd_start_alt ^ num) & 1
            even_start_alt += (even_start_alt ^ num) & 1
            odd_start_const += num & 1
            even_start_const += (num & 1) ^ 1
        return max(odd_start_alt, even_start_alt - 1, odd_start_const, even_start_const, 2)