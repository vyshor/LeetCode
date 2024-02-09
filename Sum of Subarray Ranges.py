class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        minStack, maxStack = [], []

        ans = 0
        for num in nums:
            count = 1
            while minStack and num < minStack[-1][0]:
                _, prev_count, _ = minStack.pop()
                count += prev_count

            prefix = 0
            if minStack:
                prefix = minStack[-1][2]

            prefix += count * num
            minStack.append((num, count, prefix))
            ans -= prefix

            count = 1
            while maxStack and num > maxStack[-1][0]:
                _, prev_count, _ = maxStack.pop()
                count += prev_count

            prefix = 0
            if maxStack:
                prefix = maxStack[-1][2]

            prefix += count * num
            maxStack.append((num, count, prefix))
            ans += prefix

        return ans

# Stack
# When there is a larger val, append to stack
# Else pop the stack, add the count
