class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        arr = sorted(counter.values())
        n = len(arr)
        for i, count in enumerate(arr):
            if k < count:
                return n-i
            else:
                k -= count
        return 0
