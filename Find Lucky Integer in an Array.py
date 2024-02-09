class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        maxx = -1
        for num, count in counter.items():
            if count == num:
                maxx = max(maxx, num)
        return maxx
