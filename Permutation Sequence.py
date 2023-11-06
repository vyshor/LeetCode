class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = [i for i in range(1, n + 1)]
        product = math.factorial(n - 1)
        s = ""

        while arr:
            i = k // product
            if i * product == k:
                i -= 1

            s += str(arr.pop(i))
            k %= product

            if arr:
                product //= len(arr)

        return s
