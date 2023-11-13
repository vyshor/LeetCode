class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n = len(image)
        m = len(image[0])
        prev = image[sr][sc]
        visited = set()

        def flood(i, j):
            nonlocal image, prev
            image[i][j] = color
            visited.add((i, j))

            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and image[x][y] == prev and (x, y) not in visited:
                    flood(x, y)

        flood(sr, sc)
        return image
