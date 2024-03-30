class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        last_pos = {}
        n = len(nums)
        count = 0
        left, right = 0, 0
        q = deque([])
        while right < n:
            num = nums[right]
            last_pos[num] = right
            q.append((num, right))

            while len(last_pos) > k or last_pos[q[0][0]] != q[0][1]:
                num, pos = q.popleft()
                if pos == last_pos[num]:
                    left = last_pos[num]+1
                    del last_pos[num]

            if len(last_pos) == k:
                count += q[0][1] - left + 1
            right += 1
        return count
