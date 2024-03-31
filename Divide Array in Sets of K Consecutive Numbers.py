class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        counter = Counter(nums)
        while counter:
            smallest = min(counter.keys())
            for num in range(smallest, k+smallest):
                if num not in counter:
                    return False
                counter[num] -= 1
                if counter[num] == 0:
                    del counter[num]
        return True
