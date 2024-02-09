class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num)
        # Look for 25, 75
        # Look for 00, 50

        min_op = n
        found_5 = False
        found_0 = False
        for i in range(n - 1, -1, -1):
            if found_5:
                if num[i] == "2" or num[i] == "7":
                    min_op = min(min_op, n - i - 2)
                    break
            else:
                if num[i] == '5':
                    found_5 = True

            if found_0:
                if num[i] == "0" or num[i] == "5":
                    min_op = min(min_op, n - i - 2)
                    break
            else:
                if num[i] == '0':
                    found_0 = True

        if found_0:
            min_op = min(min_op, n - 1)

        return min_op


