class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        xor2 = 0
        for num in arr2:
            xor2 ^= num

        xor1 = 0
        for num in arr1:
            xor1 ^= (num & xor2)

        return xor1
