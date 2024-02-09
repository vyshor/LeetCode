class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        ans = [1]
        while len(ans) < n:
            ans = [i * 2 - 1 for i in ans] + [i * 2 for i in ans]
        return [i for i in ans if i <= n]
