class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx = 0
        height = 0
        for delta in gain:
            height += delta
            maxx = max(maxx, height)
        return maxx
