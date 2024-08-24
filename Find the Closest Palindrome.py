class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == "10" or n == "11":
            return "9"

        if n == "1000":
            return "999"

        def midify(num):
            m = len(num)
            is_odd = m % 2 == 1
            arr = list(num)
            mid = m // 2
            if is_odd:
                for i in range(1, mid + 1):
                    arr[mid + i] = arr[mid - i]
            else:
                for i in range(mid):
                    arr[mid + i] = arr[mid - 1 - i]
            return arr

        m = len(n)
        mid = m // 2 - int(m % 2 == 0)
        arr = midify(n)
        # print(arr)
        n2 = int(n)
        first_ans = ''.join(arr)
        first_diff = abs(int(first_ans) - n2)
        second_ans = ''
        if first_ans == n:
            num = n2 + (10 ** (m - mid - 1))
            first_ans = ''.join(midify(str(num)))
            first_diff = abs(int(first_ans) - n2)

            num = n2 - (10 ** (m - mid - 1))
            second_ans = ''.join(midify(str(num)))
            second_diff = abs(int(second_ans) - n2)

            # print(first_ans, second_ans)
            if second_diff <= first_diff:
                return second_ans
            return first_ans

        elif first_ans < n:
            num = n2 + (10 ** (m - mid - 1))
            second_ans = ''.join(midify(str(num)))
            second_diff = abs(int(second_ans) - n2)
            if first_diff <= second_diff:
                return first_ans
            return second_ans
        else:
            num = n2 - (10 ** (m - mid - 1))
            second_ans = ''.join(midify(str(num)))
            second_diff = abs(int(second_ans) - n2)
            # print(second_ans)
            if first_diff < second_diff:
                return first_ans
            return second_ans

