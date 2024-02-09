class Solution:
    def grayCode(self, n: int) -> List[int]:
        prev = [0, 1]
        for i in range(2, n + 1):
            new_bit = 1 << (i - 1)
            rev = [new_bit + x for x in prev[::-1]]
            prev += rev

        return prev
