class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = []
        R = []
        pro = 1
        for num in nums:
            L.append(pro)
            pro *= num

        pro = 1
        for idx in range(n - 1, -1, -1):
            R.append(pro)
            pro *= nums[idx]

        for x in range(n):
            L[x] = L[x] * R[n - 1 - x]
        return L


# Time: O(n)
# Space: O(n)

# Runtime: 144 ms, faster than 42.03% of Python3 online submissions for Product of Array Except Self.
# Memory Usage: 20.4 MB, less than 84.00% of Python3 online submissions for Product of Array Except Self.
