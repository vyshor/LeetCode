class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        arr = []
        for k, v in counter.items():
            arr.append((v, -k))
        arr.sort()
        ans = []
        for (v, k) in arr:
            ans += [-k] * v
        return ans

