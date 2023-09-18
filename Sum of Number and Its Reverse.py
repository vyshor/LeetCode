class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        num_str = str(num)
        n = len(num_str)
        path = []

        def explorePath(i):
            for j in range(10):
                path.append(str(j))
                # print(path)

                if i + 1 == n:
                    current_int = int(''.join(path))
                    ans = current_int + int(str(current_int)[::-1]) == num
                    if ans:
                        return True
                else:
                    prevPath = explorePath(i + 1)
                    if prevPath:
                        return prevPath

                path.pop()
            return False

        return explorePath(0)
