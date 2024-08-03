class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        counter = Counter(arr)
        for num in target:
            counter[num] -= 1
            if counter[num] < 0:
                return False
        return True
