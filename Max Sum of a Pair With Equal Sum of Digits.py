class Solution:
    def max3(self, v2, x2):
        x0, x1 = v2
        if x0 <= x1 and x0 <= x2:
            return (x1, x2), x1 + x2
        elif x1 <= x0 and x1 <= x2:
            return (x0, x2), x0 + x2
        return (x0, x1), x0 + x1

    def maximumSum(self, nums: List[int]) -> int:
        matches = {}
        maxx = -1
        for num in nums:
            summ = sum([int(i) for i in str(num)])
            if summ not in matches:
                matches[summ] = (num, -num)
            else:
                matches[summ], v = self.max3(matches[summ], num)
                maxx = max(maxx, v)
        return maxx
