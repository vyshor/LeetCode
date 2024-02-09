class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        summ = 0
        stack = []

        for num in arr:
            count = 1
            while stack and stack[-1][0] >= num:
                _, prev_count, _ = stack.pop()
                count += prev_count

            prefix = 0
            if stack:
                prefix = stack[-1][2]

            stack.append((num, count, prefix + num * count))
            summ += stack[-1][-1]
            summ %= (10 ** 9 + 7)

        return summ
