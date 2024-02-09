class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def getOps(count):
            if count == 1:
                return -1
            elif count <= 3:
                return 1
            elif count == 4:
                return 2
            return count // 3 + int(0 < (count % 3) <= 2)

        counter = Counter(nums)
        total = 0
        for count in counter.values():
            diff = getOps(count)
            if diff == -1:
                return -1
            total += diff

        return total
