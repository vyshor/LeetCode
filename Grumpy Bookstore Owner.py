class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        arr = [0] * n
        total = 0
        summ = 0
        for i in range(n):
            if not grumpy[i]:
                total += customers[i]
            arr[i] = customers[i] * grumpy[i]
            if i < minutes-1:
                summ += arr[i]

        maxx = summ
        left, right = 0, minutes-1
        while right < n:
            summ += arr[right]
            maxx = max(maxx, summ)
            summ -= arr[left]
            right += 1
            left += 1
        return total + maxx
