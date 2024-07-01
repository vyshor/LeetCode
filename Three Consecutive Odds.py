class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            count += num % 2
            count *= num % 2
            if count == 3:
                return True
        return False
