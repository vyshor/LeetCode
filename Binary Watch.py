class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        n = 10  # 8,4,2,1 | 32,16,8,4,2,1
        ans = []

        def exploreLight(i, k, h, m):
            if m >= 60 or h >= 12 or k < 0:
                return

            if k == 0:
                ans.append(f"{h}:{m:02}")
                return

            if i == n:
                return

            if i < 4:
                exploreLight(i + 1, k - 1, h + (1 << (3 - i)), m)
                exploreLight(i + 1, k, h, m)
            else:
                exploreLight(i + 1, k - 1, h, m + (1 << (9 - i)))
                exploreLight(i + 1, k, h, m)

        exploreLight(0, turnedOn, 0, 0)
        return ans
