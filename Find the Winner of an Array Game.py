class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        if k >= n:
            return max(arr)

        q = deque(arr)
        num = q.popleft()

        score = 0
        while score < k:
            next_num = q.popleft()
            if next_num > num:
                num, next_num = next_num, num
                score = 1
                q.append(next_num)
            else:
                score += 1
                q.append(next_num)

        return num
