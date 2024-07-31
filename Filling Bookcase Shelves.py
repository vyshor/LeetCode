class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = {}

        def place(book, j, h):
            # print(book, j, h)
            nonlocal n, dp
            if (book, j) in dp:
                return dp[(book, j)]

            if book == n:
                return h

            thic, height = books[book]
            cost = float('inf')
            if j + thic <= shelfWidth:
                cost = place(book + 1, j + thic, max(height, h))

            if j != 0:
                cost = min(cost, h + place(book, 0, 0))

            dp[(book, j)] = cost
            return cost

        ans = place(0, 0, 0)
        # print(dp)
        return ans
