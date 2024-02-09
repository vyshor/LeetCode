class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        return 100 - 10 * (purchaseAmount // 10 + (purchaseAmount % 10 >= 5))

