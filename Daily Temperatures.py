class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, j = stack.pop()
                ans[j] = i - j
            stack.append((temp, i))
        return ans
