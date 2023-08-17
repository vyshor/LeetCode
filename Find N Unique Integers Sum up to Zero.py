class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [i for i in range(-n+(n%2)+(n%2 ^ 1),n, 2)]
