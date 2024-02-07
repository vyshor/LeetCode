class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        arr = []
        for c, count in counter.items():
            arr.append((count, c))
        arr.sort(reverse=True)
        return ''.join([c * count for (c, count) in arr])
