class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        n = len(board)
        m = len(board[0])
        n_word = len(word)

        def find(i, j, k):
            nonlocal board, visited, word
            if k == n_word:
                return True

            for (x, y) in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < n and 0 <= y < m and (x, y) not in visited and board[x][y] == word[k]:
                    visited.add((x, y))
                    ans = find(x, y, k + 1)
                    if ans:
                        return True
                    visited.remove((x, y))

            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    ans = find(i, j, 1)
                    if ans:
                        return True
                    visited.remove((i, j))
        return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        nw = len(word)

        if nw > n * m:
            return False

        dp = {}
        for i in range(1, nw):
            dp[word[i - 1] + word[i]] = []

        for i in range(m):
            for j in range(n):
                if nw == 1 and board[i][j] == word:
                    return True

                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= x < m and 0 <= y < n and board[i][j] + board[x][y] in dp:
                        dp[board[i][j] + board[x][y]].append(((i, j), (x, y)))

        if nw == 1:
            return False

        for paths in dp.values():
            if len(paths) == 0:
                return False

        q = []
        for source, target in dp[word[:2]]:
            q.append((target, {source}))

        for i in range(2, nw):
            new_q = []
            for origin, explored in q:
                for source, target in dp[word[i - 1] + word[i]]:
                    if source != origin or target in explored:
                        continue
                    else:
                        new_set = set(explored)
                        new_set.add(source)
                        new_q.append((target, new_set))

            if not new_q:
                return False
            q = new_q

        return Trueue


