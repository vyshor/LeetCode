class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        q = deque([])
        i = 0
        count = 0
        xorr = 0
        while i < n:
            if q and q[0] <= i:
                q.popleft()
                xorr ^= 1

            if nums[i] ^ xorr == 0:
                if i > n-k:
                    return -1
                xorr ^= 1
                count += 1
                q.append(i+k)
            i += 1
        return count
