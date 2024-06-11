class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counter = Counter(arr1)
        ans = []
        for num in arr2:
            for _ in range(counter[num]):
                ans.append(num)
            del counter[num]

        remaining = []
        for num, count in counter.items():
            for _ in range(count):
                remaining.append(num)
        remaining.sort()
        return ans + remaining
