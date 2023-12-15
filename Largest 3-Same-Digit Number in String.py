class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = -1
        n = len(num)
        for i in range(2, n):
            if num[i] == num[i-1] == num[i-2]:
                largest = max(largest, int(num[i-2:i+1]))
        if largest == -1:
            return ""
        return str(largest) if largest else "000"
