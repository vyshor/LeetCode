class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even, odd = 0, 0
        evenIndices = True
        while n > 0:
            if evenIndices:
                even += n % 2
            else:
                odd += n % 2

            n >>= 1
            evenIndices = not evenIndices

        return [even, odd]
