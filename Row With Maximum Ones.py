class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        count = float('-inf')
        i = 0
        for j, row in enumerate(mat):
            k = sum(row)
            if k > count:
                i = j
                count = k
        return [i, count]
