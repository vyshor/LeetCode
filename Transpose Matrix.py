class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        new_matrix = []
        for j in range(m):
            new_row = []
            for i in range(n):
                new_row.append(matrix[i][j])
            new_matrix.append(new_row)

        return new_matrix
