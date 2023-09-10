class Solution:
    def countOrders(self, n: int) -> int:
        mod = 10**9 + 7
        return (math.factorial(2*n) // (2**n)) % mod

# class Solution:
#     def countOrders(self, n: int) -> int:
#         dp = {(0, 0): 1, (1, 0): 1, (0, 1): 1}
#
#         def stateMultiple(pickups, deliveries):
#             if (pickups, deliveries) in dp:
#                 return dp[(pickups, deliveries)]
#
#             pickup = 0
#             if pickups > 0:
#                 pickup = pickups * stateMultiple(pickups - 1, deliveries + 1)
#
#             delivery = 0
#             if deliveries > 0:
#                 delivery = deliveries * stateMultiple(pickups, deliveries - 1)
#
#             dp[(pickups, deliveries)] = (pickup + delivery) % (10 ** 9 + 7)
#
#             return dp[(pickups, deliveries)]
#
#         ans = stateMultiple(n, 0)
#         # print(dp)
#         return ans

