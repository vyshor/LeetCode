class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry_over = 1
        for i in range(n-1, -1, -1):
            digits[i] += carry_over
            if digits[i] >= 10:
                digits[i] -= 10
                carry_over = 1
            else:
                carry_over = 0

        if carry_over == 1:
            return [1] + digits
        return digits
