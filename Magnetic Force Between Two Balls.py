class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def check(min_dist):
            nonlocal position, m, n
            prev = position[0]
            baskets = m-1
            for i in range(1, n):
                if position[i] - prev >= min_dist:
                    baskets -= 1
                    prev = position[i]

            return baskets <= 0

        left, right = 1, (position[-1] - position[0]) // (m-1) + 1
        maxx = 1
        while left < right:
            # print(left, right, maxx)
            mid = (left+right) // 2
            if check(mid):
                maxx = max(maxx, mid)
                if left == mid:
                    return maxx
                left = mid
            else:
                right = mid
        return maxx
