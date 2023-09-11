class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        if n < 3:
            return False

        for i in range(2, n + 1):
            for j in range(1, i):
                first, second = num[:j], num[j:i]
                if first[0] == "0" and int(first) != 0:
                    continue

                if second[0] == "0" and int(second) != 0:
                    continue

                summ = int(first) + int(second)
                summ_str = str(summ)
                summ_len = len(summ_str)

                if i + summ_len > n:
                    continue

                if num[i:i + summ_len] == summ_str:
                    idx = i + summ_len
                    if idx == n:
                        return True

                    prev, curr = int(second), summ

                    while idx <= n:
                        new_summ = prev + curr
                        new_summ_str = str(new_summ)
                        new_summ_len = len(new_summ_str)

                        if new_summ_str != num[idx:idx + new_summ_len]:
                            break

                        if idx + new_summ_len == n:
                            return True

                        idx = idx + new_summ_len
                        prev, curr = curr, new_summ

        return False



