class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        count = [0] * (k*k)
        for num in nums:
            r = num % k
            count[r*k+r] += 1
            for i in range(k):
                if i == r:
                    continue
                count[i*k+r] += (count[i*k+r] ^ 1) & 1
            for i in range(k):
                if i == r:
                    continue
                count[r*k+i] += count[r*k+i] & 1
        return max(max(count), 2)
