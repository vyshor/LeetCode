class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        maxx = 0
        if left:
            maxx = max(maxx, max(left))
        if right:
            maxx = max(maxx, n - min(right))
        return maxx
