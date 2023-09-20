class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        elif k > 0:
            summ = sum(code[1:k + 1])
            new_code = []
            for i in range(n):
                new_code.append(summ)
                summ += code[(k + 1 + i) % n] - code[(i + 1) % n]
            return new_code
        else:
            summ = sum(code[k:])
            new_code = []
            for i in range(n):
                new_code.append(summ)
                summ += code[i % n] - code[(i + k) % n]
            return new_code
