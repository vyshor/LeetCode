def gcd(a, b):
    if not a:
        return b
    return gcd(b % a, a)


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        return gcd(min(nums), max(nums))
