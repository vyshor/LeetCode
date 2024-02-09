class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        left, right = min(nums), max(nums)

        def calculateCost(target):
            total_cost = 0
            for i in range(n):
                total_cost += abs(target-nums[i]) * cost[i]
            return total_cost

        min_cost = calculateCost(left)

        while left <= right:
            mid = (left+right) // 2
            left_mid = mid-1
            right_mid = mid+1

            current_cost = calculateCost(mid)
            left_cost = calculateCost(left_mid)
            right_cost = calculateCost(right_mid)

            # print(left_mid, mid, right_mid)
            # print("Cost")
            # print(left_cost, current_cost, right_cost)

            min_cost = min(min_cost, left_cost, current_cost, right_cost)

            if left_cost > current_cost < right_cost:
                return current_cost
            elif left_cost < current_cost < right_cost:
                right = left_mid-1
            else:
                left = right_mid+1

        return min_cost
