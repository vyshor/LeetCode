class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        mid = (n // 2) + (n % 2)
        counter = list(Counter(arr).values())
        counter.sort(reverse=True)
        for i, num in enumerate(counter):
            n -= num
            if n <= mid:
                return i+1
        return 0
