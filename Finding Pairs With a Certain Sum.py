class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter = Counter(nums2)
        self.nums2 = nums2
        self.nums = Counter(nums1)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val
        self.nums2[index] = new_val

        self.counter[old_val] -= 1
        if self.counter[old_val] == 0:
            del self.counter[old_val]

        if new_val not in self.counter:
            self.counter[new_val] = 1
        else:
            self.counter[new_val] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num, num_count in self.nums.items():
            if tot - num in self.counter:
                count += self.counter[tot - num] * num_count
        return count

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)