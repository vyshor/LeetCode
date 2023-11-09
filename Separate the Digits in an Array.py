class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        arr = []
        for num in nums:
            for c in str(num):
                arr.append(int(c))
        return arr
